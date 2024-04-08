import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/mlops")

database = client['mlops']

collection = database['Products']

data = {
    "company_name": "RayRanger",
    "product": "ML Model",
}

record = collection.insert_one(data)

all_record = collection.find()

print(all_record)