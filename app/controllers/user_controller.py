from fastapi import HTTPException
from typing import List
from datetime import datetime
import uuid

from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.models.user_model import user_model


# In-memory storage
users: List[dict] = []

# -------- CREATE --------
def create_user(user: UserCreate) -> dict:
    new_user = user_model({
        "userId": str(uuid.uuid4()),
        **user.dict()
    })
    users.append(new_user)
    return new_user

# -------- GET ALL --------
def get_all_users() -> List[dict]:
    return users

# -------- GET BY ID --------
def get_user(user_id: str) -> dict:
    for u in users:
        if u["userId"] == user_id and not u["isDelete"]:
            return u
    raise HTTPException(status_code=404, detail="User not found")

# -------- UPDATE --------
def update_user(user_id: str, user_update: UserUpdate) -> dict:
    for idx, u in enumerate(users):
        if u["userId"] == user_id and not u["isDelete"]:
            updated_user = u.copy()
            updated_data = user_update.dict(exclude_unset=True)
            updated_user.update(updated_data)
            updated_user["updatedAt"] = datetime.utcnow()
            users[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# -------- DELETE --------
def delete_user(user_id: str):
    for u in users:
        if u["userId"] == user_id and not u["isDelete"]:
            u["isDelete"] = True
            u["updatedAt"] = datetime.utcnow()
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
