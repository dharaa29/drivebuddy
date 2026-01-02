from fastapi import FastAPI
from app.routers.telematics_router import router as telematics_router
from app.routers.user_router import router as user_router
from app.routers.category_router import router as category_router
from app.routers.blog_router import router as blog_router
from app.routers.tag_router import router as tag_router
from app.db.database import get_collection

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome DriveBuddy"}

# 🔹 AUTO-CREATE DATABASE ON STARTUP
@app.on_event("startup")
def startup_db():
    telematics = get_collection("telematics")
    telematics.insert_one({"status": "db_initialized"})

# Routers
app.include_router(telematics_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(blog_router)
app.include_router(tag_router)
