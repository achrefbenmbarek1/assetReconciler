import json
from QuantityReconciliation.Reconciler.domainEvent.MissingPhysicalInventoryLineItemsExtracted import (
    MissingPhysicalInventoryLineItemsExtracted,
)
from pymongo import MongoClient


def buildReportReadModelOfMissingLineItemsInPhysicalInventory(event):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["missingLineItemsInPhyscialInventoryReport"]

            if isinstance(event, MissingPhysicalInventoryLineItemsExtracted):
                missingPhysicalInventoryLineItems = event.payload[
                    "missingPhysicalInventoryLineItems"
                ]
                reconciliationId = missingPhysicalInventoryLineItems[0].get(
                    "reconciliationId", None
                )
                existing_report = collection.find_one({"_id": reconciliationId})
                if existing_report:
                    existing_inventory_ids = set(
                        item["cb"] for item in existing_report["problematicItems"]
                    )

                    newLineItems = [
                        json.dumps(item)
                        for item in missingPhysicalInventoryLineItems
                        if item["cb"] not in existing_inventory_ids
                    ]

                    if newLineItems:
                        update_operation = {
                            "$push": {"missingItems": {"$each": newLineItems}}
                        }

                        collection.update_one(
                            {"_id": reconciliationId}, update_operation
                        )
                else:
                    missingPhysicalInventoryLineItemsSerialized = [
                        json.dumps(item)
                        for item in missingPhysicalInventoryLineItems
                    ]

                    reportAboutMissingLineItemsInPhysicalInventory = {
                        "_id": reconciliationId,
                        "missingItems": missingPhysicalInventoryLineItemsSerialized,
                    }

                    collection.insert_one(
                        reportAboutMissingLineItemsInPhysicalInventory
                    )
    except Exception as e:
        raise e
