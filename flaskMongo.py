import os
import pymongo
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://root:r00tUser@myfirstcluster.obg5p.mongodb.net/myTestDB?retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find({"first": "douglas"})

documents = list(coll.find())
print(documents)

for doc in documents:
    print(conn, coll)
