from fastapi import HTTPException
import bcrypt
from app.schemas.user_schema import User
from app.db.database import get_collection

user_collection = get_collection("users")

def create_user(user: User):
    # Duplicate checks
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    if user_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password
    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user_dict = user.dict()
    user_dict["password"] = hashed_password

    user_collection.insert_one(user_dict)

    return {"message": "User created successfully"}

def get_all_users():
    users = list(user_collection.find({}, {"_id": 0}))
    return users
