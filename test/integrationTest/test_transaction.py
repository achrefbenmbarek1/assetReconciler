import pytest
from pymongo import MongoClient
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
from pymongo import ASCENDING


uriString = 'mongodb://localhost:27017/?replicaSet=rs0'

client = MongoClient(uriString)
db = client["eventstoreTest"]
collection = db["test_collection"]
collection.create_index([("abc", ASCENDING)], unique=True)


wc_majority = WriteConcern("majority", wtimeout=1000)


def callback(session):
    collection.insert_one({"abc": 8}, session=session)
    collection.insert_one({"abc": 8}, session=session)
    
def callbackValidTransaction(session):
    collection.insert_one({"abc": 1}, session=session)
    collection.insert_one({"abc": 2}, session=session)

def test_mongodb_transaction_that_doesnt_respect_the_uniqness_constrain():
    initial_count = collection.count_documents({})
    try:
        with client.start_session() as session:
            session.with_transaction(
                callback,
                read_concern=ReadConcern("local"),
                write_concern=wc_majority,
            )
        
    except Exception as e:
        print("error catched")
        
    finally:
        final_count = collection.count_documents({})
        assert initial_count == final_count 
        
def test_mongodb_transaction_that_is_valid():
    initial_count = collection.count_documents({})
    try:
        with client.start_session() as session:
            session.with_transaction(
                callback=callbackValidTransaction,
                read_concern=ReadConcern("local"),
                write_concern=wc_majority,
            )
        
    except Exception as e:
        print("error catched")
        
    finally:
        final_count = collection.count_documents({})
        client.drop_database("eventstoreTest")
        assert initial_count + 2 == final_count 

if __name__ == "__main__":
    pytest.main([__file__])
