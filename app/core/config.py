import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# MongoDB settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "telematics_db")

# Base URL for API calls (from .env)
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000/telematics/")
