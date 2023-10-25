from pymongo import MongoClient
import json
from celery import Celery

# celery = Celery("myapp")

celery = Celery(
    "myapp", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@celery.task(bind=True, max_retries=3)
def buildAmortizationReadModel(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["amortizationTableReadModel"]
            collection.insert_one(eventData)

    except Exception as e:
        print(f"Retrying task (retry {self.request.retries}): {e}")
        print(f"Task ID: {self.request.id}")
        raise self.retry(countdown=2 ** self.request.retries)


@celery.task(bind=True, max_retries=3)
def buildPhysicalInventoryReadModel(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["physicalInventoryReadModel"]
            collection.insert_one(eventData)

    except Exception as e:
        print(e) 
        raise self.retry(countdown=2 ** self.request.retries)


@celery.task(bind=True, max_retries=3)
def buildReportReadModelOfMissingLineItemsInAmortizationTable(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["readModelOfMissingLineItemsInAmortizeationTable"]

            reportIdOfProblematicLineItemsInAmortizationTable = eventData["_id"]
            existingReport = collection.find_one(
                {"_id": reportIdOfProblematicLineItemsInAmortizationTable}
            )

            if existingReport:
                missingLineItemsInAmortizationTable = json.loads(
                    eventData["missingLineItemsInAmortizationTable"]
                )
                print(missingLineItemsInAmortizationTable)

                existingLineItemsIds = set(
                    lineItem["NumFiche"]
                    for lineItem in existingReport[
                        "missingLineItemsInAmortizationTable"
                    ]
                )

                newMissingLineItems = [
                    item
                    for item in missingLineItemsInAmortizationTable
                    if item["NumFiche"] not in existingLineItemsIds
                ]

                if newMissingLineItems:
                    updateOperation = {
                        "$push": {
                            "missingLineItemsInAmortizationTable": {
                                "$each": newMissingLineItems
                            }
                        }
                    }

                    collection.update_one(
                        {"_id": reportIdOfProblematicLineItemsInAmortizationTable},
                        updateOperation,
                    )

            else:
                collection.insert_one(eventData)

    except Exception as e:
        print(e)
        raise self.retry(countdown=2 ** self.request.retries)


@celery.task(bind=True, max_retries=3)
def buildReportReadModelOfMissingLineItemsInPhysicalInventory(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["readModelOfMissingLineItemsInPhysicalInventory"]

            reportIdOfMissingLineItemsInPhysicalInventory = eventData["_id"]
            existingReport = collection.find_one(
                {"_id": reportIdOfMissingLineItemsInPhysicalInventory}
            )

            if existingReport:
                missingLineItemsInPhysicalInventoryFromCurrentReconciliation = (
                    json.loads(eventData["missingLineItemsInPhysicalInventory"])
                )
                print(missingLineItemsInPhysicalInventoryFromCurrentReconciliation)

                cbOfMissingPhysicalInventoryLineItemsThatWereReconciledInPreviousReconciliations = set(
                    lineItem["cb"]
                    for lineItem in existingReport[
                        "missingLineItemsInPhysicalInventory"
                    ]
                )

                newMissingLineItems = [
                    item
                    for item in missingLineItemsInPhysicalInventoryFromCurrentReconciliation
                    if item["cb"]
                    not in cbOfMissingPhysicalInventoryLineItemsThatWereReconciledInPreviousReconciliations
                ]

                if newMissingLineItems:
                    updateOperation = {
                        "$push": {
                            "missingLineItemsInPhysicalInventory": {
                                "$each": newMissingLineItems
                            }
                        }
                    }

                    collection.update_one(
                        {"_id": reportIdOfMissingLineItemsInPhysicalInventory},
                        updateOperation,
                    )

            else:
                collection.insert_one(eventData)

    except Exception as e:
        print(e)
        raise self.retry(countdown=2 ** self.request.retries)

@celery.task(bind=True, max_retries=3)
def buildReportReadModelOfProblematicLineItemsInPhysicalInventory(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["problematicLineItemsInPhyscialInventoryReport"]

            reportIdOfProblematicLineItemsInPhysicalInventory = eventData["_id"]
            existingReport = collection.find_one(
                {"_id": reportIdOfProblematicLineItemsInPhysicalInventory}
            )

            if existingReport:
                problematicLineItemsInPhysicalInventoryFromCurrentReconciliation = (
                    json.loads(eventData["problematicLineItemsInPhysicalInventory"])
                )
                print(problematicLineItemsInPhysicalInventoryFromCurrentReconciliation)

                cbsOfPhysicalInventoryLineItemsThatAreAlreadyProblematicFromPreviousReconciliations = set(
                    lineItem["cb"]
                    for lineItem in existingReport[
                        "missingLineItemsInPhysicalInventory"
                    ]
                )

                newMissingLineItems = [
                    item
                    for item in problematicLineItemsInPhysicalInventoryFromCurrentReconciliation
                    if item["cb"]
                    not in cbsOfPhysicalInventoryLineItemsThatAreAlreadyProblematicFromPreviousReconciliations
                ]

                if newMissingLineItems:
                    updateOperation = {
                        "$push": {
                            "missingLineItemsInPhysicalInventory": {
                                "$each": newMissingLineItems
                            }
                        }
                    }

                    collection.update_one(
                        {"_id": reportIdOfProblematicLineItemsInPhysicalInventory},
                        updateOperation,
                    )

            else:
                collection.insert_one(eventData)

    except Exception as e:
        print(e)
        raise self.retry(countdown=2 ** self.request.retries)

@celery.task(bind=True, max_retries=3)
def buildReportReadModelOfProblematicLineItemsInAmortizationTable(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["problematicLineItemsInAmortizationTable"]

            reportIdOfProblematicLineItemsInAmortizationTable = eventData["_id"]
            existingReport = collection.find_one(
                {"_id": reportIdOfProblematicLineItemsInAmortizationTable}
            )

            if existingReport:
                problematicLineItemsInAmortizationTableFromCurrentReconciliation = (
                    json.loads(eventData["problematicLineItemsInAmortizationTable"])
                )
                print(problematicLineItemsInAmortizationTableFromCurrentReconciliation)

                numFichesOfAmortizationTableLineItemsThatAreAlreadyProblematicFromPreviousReconciliations = set(
                    lineItem["NumFiche"]
                    for lineItem in existingReport[
                        "missingLineItemsInAmortizationTable"
                    ]
                )

                newMissingLineItems = [
                    item
                    for item in problematicLineItemsInAmortizationTableFromCurrentReconciliation
                    if item["NumFiche"]
                    not in numFichesOfAmortizationTableLineItemsThatAreAlreadyProblematicFromPreviousReconciliations
                ]

                if newMissingLineItems:
                    updateOperation = {
                        "$push": {
                            "missingLineItemsInPhysicalInventory": {
                                "$each": newMissingLineItems
                            }
                        }
                    }

                    collection.update_one(
                        {"_id": reportIdOfProblematicLineItemsInAmortizationTable},
                        updateOperation,
                    )

            else:
                collection.insert_one(eventData)

    except Exception as e:
        print(e)
        raise self.retry(countdown=2 ** self.request.retries)

@celery.task(bind=True, max_retries=3) 
def buildStrategyCreatorPage(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["strategyCreatorPageReadModel"]
            collection.insert_one(eventData)
    except Exception as e:
        print(e)
        raise self.retry(countdown=2 ** self.request.retries)
    

@celery.task(bind=True, max_retries=3)
def buildStrategyReadModel(self, eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["strategyReadModel"]
            query = {"_id": eventData["_id"]}
            collection.replace_one(query, eventData, upsert=True)

    except Exception as e:
        print(e)
        raise self.retry(countdown=2 ** self.request.retries)
