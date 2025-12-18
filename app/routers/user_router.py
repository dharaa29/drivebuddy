from fastapi import APIRouter
from typing import List
from app.schemas.user_schema import User
from app.controllers.user_controller import create_user, get_all_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def add_user(user: User):
    return create_user(user)

@router.get("/")
def fetch_all_users():
    return get_all_users()
