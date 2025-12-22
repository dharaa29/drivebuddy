from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import uuid

from app.schemas.blog_schema import BlogCreate, BlogUpdate, BlogResponse
from app.models.blog_model import blog_model

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

# In-memory storage
blogs: List[dict] = []

# -------- GET ALL --------
@router.get("/", response_model=List[BlogResponse])
def get_all_blogs():
    return blogs

# -------- GET BY ID --------
@router.get("/{blog_id}", response_model=BlogResponse)
def get_blog(blog_id: str):
    for blog in blogs:
        if blog["blogId"] == blog_id and not blog["isDelete"]:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

# -------- CREATE --------
@router.post("/", response_model=BlogResponse)
def create_blog(blog: BlogCreate):
    new_blog = blog_model({
        "blogId": str(uuid.uuid4()),
        **blog.dict()
    })
    blogs.append(new_blog)
    return new_blog

# -------- UPDATE --------
@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog(blog_id: str, blog_update: BlogUpdate):
    for idx, blog in enumerate(blogs):
        if blog["blogId"] == blog_id and not blog["isDelete"]:
            updated_blog = blog.copy()
            updated_data = blog_update.dict(exclude_unset=True)
            updated_blog.update(updated_data)
            updated_blog["updatedAt"] = datetime.utcnow()
            blogs[idx] = updated_blog
            return updated_blog
    raise HTTPException(status_code=404, detail="Blog not found")

# -------- DELETE --------
@router.delete("/{blog_id}")
def delete_blog(blog_id: str):
    for blog in blogs:
        if blog["blogId"] == blog_id and not blog["isDelete"]:
            blog["isDelete"] = True
            blog["updatedAt"] = datetime.utcnow()
            return {"detail": "Blog deleted"}
    raise HTTPException(status_code=404, detail="Blog not found")
