from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Load MongoDB Atlas URI from the environment variable
MONGODB_URI = os.getenv("MONGODB_URI")

client = None
db = None

async def connect_to_db():
    global client, db
    # Create a MongoDB client using the Atlas URI
    client = MongoClient(MONGODB_URI)
    db = client.get_database()  # Automatically selects the database specified in the URI

async def close_db_connection():
    global client
    client.close()
