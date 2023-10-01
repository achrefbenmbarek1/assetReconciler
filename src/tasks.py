from shared.eventInfrastructure.eventBus.EventBus import EventBus
from pymongo import MongoClient
import json
from celery import Celery

# celery = Celery("myapp")

celery = Celery(
    'myapp',
    broker='redis://localhost:6379/0', 
    backend='redis://localhost:6379/0')

# @celery.task
# def buildReadModel(events, eventBus:EventBus):
#     print("welcome to the out of process")
#     for event in events:
#         eventBus.publish(event)

@celery.task
def buildAmortizationReadModel(eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["amortizationTableReadModel"]
            # if event["eventType"] == "ReconciliationWasInitialized":
            #     amortizationDocument = {
            #         "amortizationTableLineItems": json.dumps(
            #             event.payload["amortizationTable"]
            #         ),
            #         "_id": event.reconciliationId,
            #     }
            collection.insert_one(eventData)

    except Exception as e:
        raise e

@celery.task
def buildPhysicalInventoryReadModel(eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["physicalInventoryReadModel"]
            collection.insert_one(eventData)

    except Exception as e:
        raise e

@celery.task
def buildReportReadModelOfMissingLineItemsInAmortizationTable(eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["readModelOfMissingLineItemsInAmortizeationTable"]
            print("I'm heeere")

            reportIdOfProblematicLineItemsInPhysicalInventory = eventData[
                "_id"
            ]
            print("I'm inspecting")
            existingReport = collection.find_one(
                {"_id": reportIdOfProblematicLineItemsInPhysicalInventory}
            )
            
            if existingReport:
                missingLineItemsInAmortizationTable = json.loads(
                    eventData["missingLineItemsInAmortizationTable"]
                )
                print("guess who is out of process")
                print(missingLineItemsInAmortizationTable)
                
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
                print("are we here")
                collection.insert_one(eventData)

    except Exception as e:
        raise e

@celery.task
def buildStrategyReadModel(eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["strategyReadModel"]
            query = { "_id": eventData["_id"] }
            collection.replace_one(query, eventData, upsert= True)

    except Exception as e:
        raise e
