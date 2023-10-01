from pymongo import MongoClient

from celery import shared_task


@shared_task
def buildAmortizationReadModelHandler(eventData):
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
