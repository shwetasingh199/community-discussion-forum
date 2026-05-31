from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(
    os.getenv("MONGO_URI")
)

db = client["community_forum"]

users = db["users"]
discussions = db["discussions"]
comments = db["comments"]
messages = db["messages"]
notifications = db["notifications"]