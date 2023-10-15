import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://margi:<Password>@bdmatrixteste.y481m6t.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

for dbname in client.list_database_names():
    print(dbname)

db = client.diotest

# collection = db.produtos

print(db.list_collection_names())

post = {
    "autor": "Regi",
    "texto": "Sempre evoluíndo",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.now(datetime.UTC)
}

posts = db.posts
# post_id=posts.insert_one(post).inserted_id
# print(post_id)

print(db.posts)
print(db.posts.find_one())

# pprint.pprint(db.posts.find_one())

# para adicionar varios registros do tipo vetor
# result =posts.insert_many(new_posts)
# result(result.inserted_ids)


for item in posts.find():
    print(item)

print(f"Total: {posts.count_documents({})}")
# deletar
# db.posts.drop()

# posts.delete_one({"nome":"Regi"})

# apagando database
client.drop_database('teste')
