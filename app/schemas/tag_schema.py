from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.enums.status_enum import Status

class TagCreate(BaseModel):
    name: str
    status: Optional[Status] = Status.Active
    createdBy: str
    description: Optional[str] = None
    slug: str  # ✅ Add this

class TagUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[Status] = None
    description: Optional[str] = None

class TagResponse(BaseModel):
    tagId: str
    name: str
    status: Status
    description: Optional[str] = None
    isDelete: bool
    createdBy: str
    updatedBy: Optional[str] = None
    createdAt: datetime
    updatedAt: Optional[datetime] = None
