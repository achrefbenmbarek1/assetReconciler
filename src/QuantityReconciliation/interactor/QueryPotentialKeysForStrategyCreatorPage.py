from pymongo import MongoClient


class QueryPotentialKeysForStrategyCreatorPage:
    def queryStrategyCreatedPage(self, id):
        try:
            with MongoClient("mongodb://localhost:27017/") as mongoClient:
                db = mongoClient["readModels"]
                collection = db["strategyCreatorPageReadModel"]
                document = collection.find_one({"_id": id})
                if (document is None):
                    raise Exception("problem with the strategy creator database")
                potentialKeys = document.get("strategyPotentialKeys", [])
                print(type(potentialKeys))
                return potentialKeys

        except Exception as e:
            raise e
