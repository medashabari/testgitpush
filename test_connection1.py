import pymongo
client = pymongo.MongoClient("mongodb+srv://system:system@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
d = {
    "name":"Shabarish",
    "email" : "shabari@gmail.com",
    "surname" : "meda"
}
db = client['mongotest1']
coll =db['test2']
coll.insert_one(d)
