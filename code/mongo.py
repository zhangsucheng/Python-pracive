from pymongo import MongoClient

client = MongoClient('mongodb://114.215.151.210:27017', username="admin", password="suziyoudian")
dblist = client.list_database_names()
print(dblist)
testdb = client["test"]
collection = testdb["role"]
print(collection)