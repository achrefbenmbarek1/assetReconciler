from QuantityReconciliation.Reconciler.domainEvent.ProblematicLineItemsInAmortizationTableExtracted import (
    ProblematicLineItemsInAmortizationTableExtracted,
)
from pymongo import MongoClient
import json


def buildAmortizationTableReportReadModelOfProblematicLineItems(event):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["problematicLineItemsInAmortizationTableReport"]

            if isinstance(event, ProblematicLineItemsInAmortizationTableExtracted):
                problematic_items = (
                    event.payload["problematicLineItemsInAmortizationTable"] 
                )
                reconciliationId = problematic_items[0].get("reconciliationId", None)
                existing_report = collection.find_one({"_id": reconciliationId})
                if existing_report:
                    existing_inventory_ids = set(
                        item["NumFiche"] for item in existing_report["problematicItems"]
                    )

                    newLineItems = [
                        item
                        for item in problematic_items
                        if item["NumFiche"] not in existing_inventory_ids
                    ]

                    if newLineItems:
                        update_operation = {
                            "$push": {"problematicItems": {"$each": newLineItems}}
                        }

                        collection.update_one(
                            {"_id": reconciliationId}, update_operation
                        )
                else:
                    reportAboutProblematicLineItemsInPhysicalInventory = {
                        "_id": reconciliationId,
                        "problematicItems": json.dumps(problematic_items),
                    }

                    collection.insert_one(
                        reportAboutProblematicLineItemsInPhysicalInventory
                    )
    except Exception as e:
        raise e
