from fastapi import FastAPI
from app.routers.telematics_router import router as telematics_router
from app.routers.user_router import router as user_router
from app.routers.category_router import router as category_router

app = FastAPI()

app.include_router(telematics_router)
app.include_router(user_router)
app.include_router(category_router)
