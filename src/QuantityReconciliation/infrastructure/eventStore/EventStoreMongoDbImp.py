import json
from QuantityReconciliation.infrastructure.eventStore.DomainEventDataMapper import DomainEventDataMapper
from QuantityReconciliation.infrastructure.eventStore.EventStore import EventStore
from pymongo import MongoClient
from shared.eventInfrastructure.DomainEvent import DomainEvent
from pymongo.errors import ConnectionFailure


class EventStoreMongoDbImp(EventStore):
    def __init__(self, mongoUri, dbName, collectionName):
        self.mongoUri = mongoUri
        self.dbName = dbName
        self.collectionName = collectionName
        self.collection = None
        
    def _connect(self):
            try:
                self.mongoClient = MongoClient(self.mongoUri)
                self.db = self.mongoClient[self.dbName]
                self.collection = self.db[self.collectionName]
            except ConnectionFailure as e:
                raise e
            
    def _disconnect(self):
        if hasattr(self, 'mongo_client'):
            self.mongoClient.close
            
    def appendEvents(self, reconciliationId, domainEvents, expectedVersion) -> None:
        # currentVersion = self.collection.count_documents({"reconciliationId": reconciler.reconciliationState.reconciliationId}) 
        # if currentVersion + 1 != reconciler.reconciliationState.version:
        #     raise Exception("concurrency problem")
        # eventsData = []
        # for event in reconciler.domainEvents:
        #     eventData = {
        #         "reconciliationId": event.reconciliationId,
        #         "payload": event.payload,
        #         "timestamp": event.timestamp,
        #         "eventType": type(event)
        #     }
        #     if event.eventId is not None:
        #         eventData["_id"] = event.eventId
        #     eventsData.append(eventData)   
        # if(eventsData != []):
        #     self.collection.insert_many(eventsData)
        try:
            self._connect()
            if self.collection is None:
                raise ConnectionFailure
            with self.mongoClient.start_session() as session:
                try:
                    session.start_transaction()

                    currentVersion = self.collection.count_documents(
                        {"reconciliationId": reconciliationId}
                    ) + len(domainEvents) - 1
                    print("current version", currentVersion)
                    print("expected version", expectedVersion)
                    if currentVersion != expectedVersion:
                        raise Exception("Concurrency problem")

                    eventsData = []
                    for event in domainEvents:
                        eventData = {
                            "reconciliationId": event.reconciliationId,
                            "payload": json.dumps(event.payload),
                            "timestamp": event.timestamp,
                            "eventType": type(event).__name__,
                            "_id": event.eventId
                        }
                        # if event.eventId is not None:
                        #     eventData["_id"] = event.eventId
                        eventsData.append(eventData)

                    if eventsData:
                        self.collection.insert_many(eventsData, session=session)

                    session.commit_transaction()
                except Exception as e:
                    session.abort_transaction()
                    raise e 
            
        except Exception as e:
            raise e
        
        finally:
            self._disconnect()


    def loadEvents(self, reconciliationId) -> list[DomainEvent]:
        try:
            self._connect()
            if self.collection is None:
                raise ConnectionFailure
            events = []
            cursor = self.collection.find({"reconciliationId": reconciliationId}).sort("timestamp")
            for eventData in cursor:
                eventFactory:DomainEventDataMapper = DomainEventDataMapper()
                event = eventFactory.createDomainEvent(eventData)
                events.append(event)
                
            return events
            
        except Exception as e:
            raise e
        finally:
            self._disconnect()
