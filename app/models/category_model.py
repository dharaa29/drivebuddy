from datetime import datetime
from app.schemas.category_schema import StatusEnum


def category_model(data: dict) -> dict:
    return {
        "categoryId": data["categoryId"],
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
