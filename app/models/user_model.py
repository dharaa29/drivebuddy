from sqlalchemy import Column, String, Boolean, Enum
from app.db.database import Base
import enum


class StatusEnum(enum.Enum):
    Active = "Active"
    Inactive = "Inactive"


class User(Base):
    __tablename__ = "users"

    userId = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String, unique=True, index=True)
    mobileNo = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.Active)
    isDelete = Column(Boolean, default=False)
    createdBy = Column(String)
    updatedBy = Column(String, nullable=True)
