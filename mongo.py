import pymongo
from pymongo import MongoClient

cluster = MongoClient ("mongodb+srv://root:r00tUser@myfirstcluster.obg5p.mongodb.net/MyTestDB?retryWrites=true&w=majority")
db = cluster ["myTestDB"]
collection = db ["myTestDB"]

post4 = {"_id": "ID", "firstname": "Delroy", "lastname": "Brown"}
post3 = {"_id": "OLDEST ID", "firstname": "Mary", "lastname": "Butt"}

results = collection.insert_many([post4, post3])