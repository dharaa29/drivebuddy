from datetime import datetime
from app.enums.status_enum import Status

def user_model(data: dict) -> dict:
    return {
        "userId": data.get("userId"),
        "username": data["username"],
        "password": data["password"],  # hash before storing
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "email": data["email"],
        "mobileNo": data["mobileNo"],
        "status": data.get("status", Status.Active),  # ✅ Fixed
        "isDelete": data.get("isDelete", False),
        "createdBy": data["createdBy"],
        "updatedBy": data.get("updatedBy"),
        "createdAt": datetime.utcnow(),
        "updatedAt": None,
    }
