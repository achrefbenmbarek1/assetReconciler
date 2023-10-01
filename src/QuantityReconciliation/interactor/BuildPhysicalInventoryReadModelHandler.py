from celery import shared_task
from pymongo import MongoClient



@shared_task
def buildPhysicalInventoryReadModel(eventData):
    try:
        with MongoClient("mongodb://localhost:27017/") as mongoClient:
            db = mongoClient["readModels"]
            collection = db["physicalInventoryReadModel"]
            print("we're doing it finally")
            # if event["eventType"] == "ReconciliationWasInitialized":
            # physicalInventoryDocument = {
            #     "amortizationTableLineItems": json.dumps(
            #         event.payload["physicalInventory"]
            #     ),
            #     "_id": event.reconciliationId,
            # }
            collection.insert_one(eventData)

    except Exception as e:
        raise e
