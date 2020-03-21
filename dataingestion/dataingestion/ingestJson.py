import pymongo

mng_client = pymongo.MongoClient("mongodb://root:rootpassword@127.0.0.1:27017/")
mng_db = mng_client["covid"]  # Replace mongo db name
collection_name = "covidset"  # Replace mongo db collection name
db_cm = mng_db[collection_name]

# Get the data from JSON file
data_json1 = """{
   "appId": 1,
   "currentPos": { "type": "Point", "coordinates": [ 73.93800169229507,
          18.52394103864915 ] },
   "serverity": "infected",
   "place":"Greenfield"
}"""

data_json2 = """{
   "appId": 2,
   "currentPos": { "type": "Point", "coordinates": [ 73.93562793731688,
          18.51863828766966 ] },
   "serverity": "infected",
   "place":"Amanor Mall"
}
"""

data_json3 = """{
   "appId": 3,
   "currentPos": { "type": "Point", "coordinates": [ 73.92857909202576,
          18.515677831441508 ] },
   "serverity": "infected",
   "place":"Tower 12"
}
"""

data_json4 = """{
   "appId": 4,
   "currentPos": { "type": "Point", "coordinates": [ 73.95080924034119,
          18.551372836132593 ] },
   "serverity": "infected",
   "place":"Kharadi,Eon IT"
}
"""


# Insert Data
db_cm.remove()
db_cm.insert(eval(data_json1))
db_cm.insert(eval(data_json2))
db_cm.insert(eval(data_json3))
db_cm.insert(eval(data_json4))
# Query data
print(db_cm.find({"appId": 1}))


# db_cm.find(
#    {
#      location:
#        { $near:
#           {
#             $geometry: { type: "Point",  coordinates: [ -73.9667, 40.78 ] },
#             $minDistance: 1000,
#             $maxDistance: 5000
#           }
#        }
#    }
# )
