from pymongo import MongoClient

client = MongoClient("mongodb+srv://Blogpost:Computer333@cluster0.ve2nnja.mongodb.net/mydatabase?retryWrites=true&w=majority")

db = client.mypost

collections_post = db["myapp"]

collection_comments = db["comments"]