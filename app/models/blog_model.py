from datetime import datetime
from app.enums.status_enum import BlogStatus

def blog_model(data: dict) -> dict:
    return {
        "blogId": data.get("blogId"),
        "customerId": data["customerId"],
        "tagId": data["tagId"],
        "categoryId": data["categoryId"],
        "title": data["title"],
        "shortDescription": data["shortDescription"],
        "content": data["content"],
        "image": data["image"],
        "publishedAt": data.get("publishedAt"),
        "status": data.get("status", BlogStatus.Draft),
        "isDelete": False,
        "createdBy": data["createdBy"],
        "updatedBy": None,
        "createdAt": datetime.utcnow(),
        "updatedAt": None,
    }
