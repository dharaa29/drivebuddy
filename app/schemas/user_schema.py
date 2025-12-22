# app/schemas/user_schema.py

from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.enums.status_enum import Status


# Schema for creating a user
class UserCreate(BaseModel):
    userId: str = Field(..., description="Unique user ID")
    username: str
    password: str  # raw password, will be hashed before storing
    firstName: str
    lastName: str
    email: EmailStr
    mobileNo: str
    status: Status = Status.Active  # default to Active
    isDelete: bool = False
    createdBy: str
    updatedBy: Optional[str] = None  # optional field

# Schema for updating a user
class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None  # optional, hash before saving
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[EmailStr] = None
    mobileNo: Optional[str] = None
    status: Optional[Status] = None
    isDelete: Optional[bool] = None
    updatedBy: Optional[str] = None

# Schema for returning user info
class UserResponse(BaseModel):
    userId: str
    username: str
    firstName: str
    lastName: str
    email: EmailStr
    mobileNo: str
    status: Status
    isDelete: bool
    createdBy: str
    updatedBy: Optional[str] = None  # make optional for safety

    class Config:
        # Pydantic v2 changed orm_mode -> from_attributes
        from_attributes = True
