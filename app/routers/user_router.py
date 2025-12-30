from fastapi import APIRouter
from typing import List
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.controllers.user_controller import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create(user: UserCreate):
    return create_user(user)


@router.get("/", response_model=List[UserResponse])
def get_all():
    return get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id: str):
    return get_user_by_id(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: str, user: UserUpdate):
    return update_user(user_id, user)


@router.delete("/{user_id}")
def delete(user_id: str):
    return delete_user(user_id)
