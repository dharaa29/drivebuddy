from datetime import datetime
from app.enums.status_enum import StatusEnum

def tag_model(data: dict) -> dict:
    return {
        "tagId": data.get("tagId"),
        "name": data["name"],
        "description": data.get("description"),
        "slug": data["slug"],
        "status": data.get("status", StatusEnum.Active),
        "isDelete": False,
        "createdBy": data["createdBy"],
        "updatedBy": None,
        "createdAt": datetime.utcnow(),
        "updatedAt": None,
    }
