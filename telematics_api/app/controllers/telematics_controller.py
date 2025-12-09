# app/controllers/telematics_controller.py
from ..db.collections import telematics_collection
from app.schemas.telematics_schema import TelematicsCreate

def create_telematics(data: TelematicsCreate):
    # Insert into MongoDB
    telematics_collection.insert_one(data.dict())
    return "Telematics data added successfully"

def get_all_telematics():
    # Fetch all documents from MongoDB
    return list(telematics_collection.find({}, {"_id": 0}))
