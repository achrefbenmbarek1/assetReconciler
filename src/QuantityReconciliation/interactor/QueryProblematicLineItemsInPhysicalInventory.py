from pymongo import MongoClient


class QueryProblematicLineItemsInPhysicalInventory:
    def QueryProblematicLineItemsInPhysicalInventory(self, id):
        try:
            with MongoClient("mongodb://localhost:27017/") as mongoClient:
                db = mongoClient["readModels"]
                collection = db["problematicLineItemsInPhyscialInventoryReport"]
                document = collection.find_one({"_id": id})
                if (document is None):
                    raise Exception("problem with the problematic line items database")
                print(document)
                return document

        except Exception as e:
            raise e

