from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import uuid

from app.schemas.blog_schema import BlogCreate, BlogUpdate, BlogResponse
from app.enums.status_enum import BlogStatus

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

blogs_db: List[BlogResponse] = []

@router.get("/", response_model=List[BlogResponse])
def get_all_blogs():
    return [blog for blog in blogs_db if not blog.isDelete]

@router.get("/{blog_id}", response_model=BlogResponse)
def get_blog(blog_id: str):
    for blog in blogs_db:
        if blog.blogId == blog_id and not blog.isDelete:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.post("/", response_model=BlogResponse)
def create_blog(blog: BlogCreate):
    new_blog = BlogResponse(
        blogId=str(uuid.uuid4()),
        customerId=blog.customerId,
        tagId=blog.tagId,
        categoryId=blog.categoryId,
        title=blog.title,
        shortDescription=blog.shortDescription,
        content=blog.content,
        image=blog.image,
        publishedAt=blog.publishedAt,
        status=blog.status,
        isDelete=False,
        createdBy=blog.createdBy,
        updatedBy=None,
        createdAt=datetime.utcnow(),
        updatedAt=None
    )
    blogs_db.append(new_blog)
    return new_blog

@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog(blog_id: str, blog_update: BlogUpdate):
    for blog in blogs_db:
        if blog.blogId == blog_id and not blog.isDelete:
            if blog_update.title: blog.title = blog_update.title
            if blog_update.shortDescription: blog.shortDescription = blog_update.shortDescription
            if blog_update.content: blog.content = blog_update.content
            if blog_update.image: blog.image = blog_update.image
            if blog_update.publishedAt: blog.publishedAt = blog_update.publishedAt
            if blog_update.status: blog.status = blog_update.status
            blog.updatedBy = blog_update.updatedBy
            blog.updatedAt = datetime.utcnow()
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/{blog_id}")
def delete_blog(blog_id: str):
    for blog in blogs_db:
        if blog.blogId == blog_id and not blog.isDelete:
            blog.isDelete = True
            blog.updatedAt = datetime.utcnow()
            return {"detail": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")
