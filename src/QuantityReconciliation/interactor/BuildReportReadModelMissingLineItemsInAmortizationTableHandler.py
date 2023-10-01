import json
from celery import shared_task
from pymongo import MongoClient


@shared_task
def buildReportReadModelOfMissingLineItemsInAmortizationTable(eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["readModelOfMissingLineItemsInAmortizeationTable"]

            reportIdOfProblematicLineItemsInPhysicalInventory = eventData[
                "reconciliationId"
            ]
            existingReport = collection.find_one(
                {"_id": reportIdOfProblematicLineItemsInPhysicalInventory}
            )

            if existingReport:
                missingLineItemsInAmortizationTable = json.loads(
                    eventData["missingLineItemsInAmortizationTable"]
                )
                
                existingLineItemsIds = set(
                    lineItem["NumFiche"] for lineItem in existingReport["missingLineItemsInAmortizationTable"]
                )

                newMissingLineItems = [
                    item
                    for item in missingLineItemsInAmortizationTable
                    if item["NumFiche"] not in existingLineItemsIds
                ]

                if newMissingLineItems:
                    updateOperation = {
                        "$push": {"missingLineItemsInAmortizationTable": {"$each": newMissingLineItems}}
                    }

                    collection.update_one(
                        {"_id": reportIdOfProblematicLineItemsInPhysicalInventory},
                        updateOperation,
                    )

                else:
                    collection.insert_one(eventData)

    except Exception as e:
        raise e
