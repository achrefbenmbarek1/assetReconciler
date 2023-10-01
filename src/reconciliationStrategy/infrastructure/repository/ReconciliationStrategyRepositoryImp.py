from pymongo import MongoClient
from reconciliationStrategy.entity.ReconciliationStrategy import ReconciliationStrategy
from reconciliationStrategy.infrastructure.repository.ReconciliationStrategyRepository import ReconciliationStrategyRepository


class ReconciliationStrategyRepositoryImp(ReconciliationStrategyRepository):
    def __init__(self, mongo_uri, db_name, collection_name):
        self.mongo_client = MongoClient(mongo_uri)
        self.db = self.mongo_client[db_name]
        self.collection = self.db[collection_name]

    def save(self,reconciliationStrategy:ReconciliationStrategy) -> None:
        document = self.collection.find_one({"_id": reconciliationStrategy.id},{"version":1, "_id":0}) 
        currentVersion = 0
        
        if document is not None:
            currentVersion = document.get("version")
        
        if currentVersion + 1 != reconciliationStrategy.version:
            raise Exception("concurrency problem in reconciliationStrategy chooser")
        
        strategyData = {
            "_id": reconciliationStrategy.id,
            "orderedCycles": reconciliationStrategy.orderedCycles,
            "version": reconciliationStrategy.version
        }
            
        self.collection.insert_one(strategyData)

