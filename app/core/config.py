import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# MongoDB settings
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Base URL for API calls
BASE_URL = os.getenv("BASE_URL")
