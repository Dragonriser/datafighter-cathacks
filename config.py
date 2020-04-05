import pymongo
# mongo = pymongo.MongoClient('mongodb+srv://shivaylamba:shivaylamba@cluster0-dxlmn.gcp.mongodb.net/test', maxPoolSize=50, connect=False)
# db = pymongo.database.Database(mongo, 'datafighter')
# col = pymongo.collection.Collection(db, 'tweets')
# col_results = json.loads(dumps(col.find().limit(5).sort("time", -1)))



client = pymongo.MongoClient("mongodb+srv://shivaylamba:shivaylamba@cluster0-dxlmn.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
