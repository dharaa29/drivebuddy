from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import datetime


class StatusEnum(str, Enum):
    Active = "Active"
    Inactive = "Inactive"


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    slug: str
    status: StatusEnum = StatusEnum.Active


class CategoryCreate(CategoryBase):
    createdBy: str


class CategoryUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    slug: Optional[str]
    status: Optional[StatusEnum]
    updatedBy: str


class CategoryResponse(CategoryBase):
    categoryId: str
    isDelete: bool
    createdBy: str
    updatedBy: Optional[str] = None
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True
