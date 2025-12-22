from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from app.enums.status_enum import Status

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None
    slug: str
    status: Status = Status.Active
    createdBy: str


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    status: Optional[Status] = None
    updatedBy: str


class CategoryResponse(BaseModel):
    categoryId: str
    name: str
    description: Optional[str]
    slug: str
    status: Status
    isDelete: bool
    createdBy: str
    updatedBy: Optional[str]
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        from_attributes = True   # Pydantic v2
