from pymongo import MongoClient
from ..core.config import MONGO_URI, DB_NAME

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_collection(name: str):
    """
    Return a MongoDB collection by name
    """
    return db[name]
