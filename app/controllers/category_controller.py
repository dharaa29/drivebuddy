import uuid
from datetime import datetime
from app.models.category_model import category_model
from app.db.database import get_collection

# MongoDB collection
category_collection = get_collection("categories")


def create_category(payload: dict):
    """Create a new category and save to MongoDB"""
    payload["categoryId"] = str(uuid.uuid4())
    payload["isDelete"] = False
    payload["createdAt"] = datetime.utcnow()
    payload["updatedAt"] = None
    category = category_model(payload)
    category_collection.insert_one(category)
    return category


def get_all_categories():
    """Return all non-deleted categories"""
    categories = []
    for category in category_collection.find({"isDelete": False}):
        category["_id"] = str(category["_id"])
        categories.append(category)
    return categories


def get_category_by_id(category_id: str):
    """Get a single category by categoryId"""
    category = category_collection.find_one(
        {"categoryId": category_id, "isDelete": False},
        {"_id": 0}
    )
    return category


def update_category(category_id: str, payload: dict):
    """Update a category"""
    payload["updatedAt"] = datetime.utcnow()
    result = category_collection.update_one(
        {"categoryId": category_id, "isDelete": False},
        {"$set": payload}
    )
    return result.modified_count > 0


def delete_category(category_id: str, updated_by: str):
    """Soft delete a category"""
    result = category_collection.update_one(
        {"categoryId": category_id},
        {
            "$set": {
                "isDelete": True,
                "updatedBy": updated_by,
                "updatedAt": datetime.utcnow(),
            }
        }
    )
    return result.modified_count > 0
