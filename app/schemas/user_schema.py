from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class Status(str, Enum):
    Active = "Active"
    Inactive = "Inactive"

class User(BaseModel):
    userId: str
    username: str
    password: str
    firstName: str
    lastName: str
    email: EmailStr
    mobileNo: str
    status: Status
    isDelete: bool = False
    createdBy: str
    updatedBy: Optional[str] = None

class UserResponse(User):
    pass  # Can add fields to hide password if needed
