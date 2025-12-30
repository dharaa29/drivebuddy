from fastapi import HTTPException
from typing import List
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse

# Temporary in-memory storage
users_db: List[UserResponse] = []


def create_user(user: UserCreate) -> UserResponse:
    new_user = UserResponse(
        userId=user.userId,
        username=user.username,
        firstName=user.firstName,
        lastName=user.lastName,
        email=user.email,
        mobileNo=user.mobileNo,
        status=user.status,
        isDelete=user.isDelete,
        createdBy=user.createdBy,
        updatedBy=user.updatedBy
    )
    users_db.append(new_user)
    return new_user


def get_all_users() -> List[UserResponse]:
    return users_db


def get_user_by_id(user_id: str) -> UserResponse:
    for user in users_db:
        if user.userId == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


def update_user(user_id: str, user_data: UserUpdate) -> UserResponse:
    for index, user in enumerate(users_db):
        if user.userId == user_id:
            updated_user = user.copy(update=user_data.dict(exclude_unset=True))
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


def delete_user(user_id: str):
    for index, user in enumerate(users_db):
        if user.userId == user_id:
            users_db.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
