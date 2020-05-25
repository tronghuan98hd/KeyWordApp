import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["test_db"]
col = db["intents"]

