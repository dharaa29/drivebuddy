from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.enums.status_enum import BlogStatus


class BlogCreate(BaseModel):
    customerId: str
    tagId: str
    categoryId: str
    title: str
    shortDescription: str
    content: str
    image: str
    publishedAt: Optional[datetime] = None
    status: BlogStatus = BlogStatus.Draft
    createdBy: str

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    shortDescription: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None
    publishedAt: Optional[datetime] = None
    status: Optional[BlogStatus] = None
    updatedBy: str

class BlogResponse(BaseModel):
    blogId: str
    customerId: str
    tagId: str
    categoryId: str
    title: str
    shortDescription: str
    content: str
    image: str
    publishedAt: Optional[datetime]
    status: BlogStatus
    isDelete: bool
    createdBy: str
    updatedBy: Optional[str]
    createdAt: datetime
    updatedAt: Optional[datetime]

    model_config = {"from_attributes": True}
