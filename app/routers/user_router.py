from fastapi import APIRouter
from typing import List
from app.schemas.user_schema import UserCreate, UserResponse
from app.controllers.user_controller import create_user, get_all_users

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
