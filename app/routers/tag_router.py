from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import uuid

from app.schemas.tag_schema import TagCreate, TagUpdate, TagResponse
from app.enums.status_enum import Status

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)

tags_db: List[TagResponse] = []

@router.get("/", response_model=List[TagResponse])
def get_all_tags():
    return [tag for tag in tags_db if not tag.isDelete]

@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(tag_id: str):
    for tag in tags_db:
        if tag.tagId == tag_id and not tag.isDelete:
            return tag
    raise HTTPException(status_code=404, detail="Tag not found")

@router.post("/", response_model=TagResponse)
def create_tag(tag: TagCreate):
    new_tag = TagResponse(
        tagId=str(uuid.uuid4()),
        name=tag.name,
        description=tag.description,
        slug=tag.slug,
        status=tag.status,
        isDelete=False,
        createdBy=tag.createdBy,
        updatedBy=None,
        createdAt=datetime.utcnow(),
        updatedAt=None
    )
    tags_db.append(new_tag)
    return new_tag

@router.put("/{tag_id}", response_model=TagResponse)
def update_tag(tag_id: str, tag_update: TagUpdate):
    for tag in tags_db:
        if tag.tagId == tag_id and not tag.isDelete:
            if tag_update.name: tag.name = tag_update.name
            if tag_update.description: tag.description = tag_update.description
            if tag_update.slug: tag.slug = tag_update.slug
            if tag_update.status: tag.status = tag_update.status
            tag.updatedBy = tag_update.updatedBy
            tag.updatedAt = datetime.utcnow()
            return tag
    raise HTTPException(status_code=404, detail="Tag not found")

@router.delete("/{tag_id}")
def delete_tag(tag_id: str):
    for tag in tags_db:
        if tag.tagId == tag_id and not tag.isDelete:
            tag.isDelete = True
            tag.updatedAt = datetime.utcnow()
            return {"detail": "Tag deleted successfully"}
    raise HTTPException(status_code=404, detail="Tag not found")
