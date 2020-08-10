import pymongo
from pymongo import MongoClient

# Posts info to database on MongoDB
cluster = MongoClient ("mongodb+srv://root:r00tUser@myfirstcluster.obg5p.mongodb.net/MyTestDB?retryWrites=true&w=majority")
db = cluster ["myTestDB"]
collection = db ["myTestDB"]

post3 = {"_id": "Countys", "Country Name": "England"}

results = collection.insert_one(post3)

print("The data in the database is:") 
cursor = collection.find()  
for record in cursor:  
    print(results)