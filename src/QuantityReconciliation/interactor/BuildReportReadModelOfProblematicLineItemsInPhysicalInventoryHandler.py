import json
from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInPhysicalInventoryExtracted import (
    ProblematicLineItemsInPhysicalInventoryExtracted,
)
from pymongo import MongoClient


def buildReportReadModelOfProblematicPhysicalInventory(event):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["problematicLineItemsInPhyscialInventoryReport"]

            if isinstance(event, ProblematicLineItemsInPhysicalInventoryExtracted):
                problematic_items = event.payload[
                    "problematicLineItemsInPhysicalInventory"
                ]
                reconciliation_id = problematic_items[0].get("reconciliationId", None)
                existing_report = collection.find_one({"_id": reconciliation_id})
                if existing_report:
                    existing_inventory_ids = set(
                        item["cb"] for item in existing_report["problematicItems"]
                    )

                    newLineItems = [
                        item
                        for item in problematic_items
                        if item["cb"] not in existing_inventory_ids
                    ]

                    if newLineItems:
                        update_operation = {
                            "$push": {"problematicItems": {"$each": newLineItems}}
                        }

                        collection.update_one(
                            {"_id": reconciliation_id}, update_operation
                        )
                else:
                    reportAboutProblematicLineItemsInPhysicalInventory = {
                        "_id": reconciliation_id,
                        "problematicItems": json.dumps(problematic_items),
                    }

                    collection.insert_one(
                        reportAboutProblematicLineItemsInPhysicalInventory
                    )
    except Exception as e:
        raise e
