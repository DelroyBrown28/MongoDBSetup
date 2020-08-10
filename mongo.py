import pymongo
from pymongo import MongoClient

# Posts info to database on MongoDB
cluster = MongoClient ("mongodb+srv://root:r00tUser@myfirstcluster.obg5p.mongodb.net/MyTestDB?retryWrites=true&w=majority")
db = cluster ["myTestDB"]
collection = db ["myTestDB"]

post4 = {"_id": "ID", "firstname": "Delroy", "lastname": "Brown"}
post3 = {"_id": "OLDEST ID", "firstname": "Mary", "lastname": "Butt"}
post6 = {"_id": "Goodbye, World!", "type": "WebDev"}
post7 = {"_id": "Hair colour", "Colour": "Brown"}

results = collection.insert_one(post7)

print("The data in the database is:") 
cursor = collection.find()  
for record in cursor:  
    print(post7)