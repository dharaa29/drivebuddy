from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import uuid

from app.schemas.tag_schema import TagCreate, TagUpdate, TagResponse
from app.models.tag_model import tag_model

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)

# In-memory storage
tags: List[dict] = []

# -------- GET ALL --------
@router.get("/", response_model=List[TagResponse])
def get_all_tags():
    return tags

# -------- GET BY ID --------
@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(tag_id: str):
    for tag in tags:
        if tag["tagId"] == tag_id and not tag["isDelete"]:
            return tag
    raise HTTPException(status_code=404, detail="Tag not found")

# -------- CREATE --------
@router.post("/", response_model=TagResponse)
def create_tag(tag: TagCreate):
    new_tag = tag_model({
        "tagId": str(uuid.uuid4()),
        **tag.dict()
    })
    tags.append(new_tag)
    return new_tag

# -------- UPDATE --------
@router.put("/{tag_id}", response_model=TagResponse)
def update_tag(tag_id: str, tag_update: TagUpdate):
    for idx, tag in enumerate(tags):
        if tag["tagId"] == tag_id and not tag["isDelete"]:
            updated_tag = tag.copy()
            updated_data = tag_update.dict(exclude_unset=True)
            updated_tag.update(updated_data)
            updated_tag["updatedAt"] = datetime.utcnow()
            tags[idx] = updated_tag
            return updated_tag
    raise HTTPException(status_code=404, detail="Tag not found")

# -------- DELETE --------
@router.delete("/{tag_id}")
def delete_tag(tag_id: str):
    for tag in tags:
        if tag["tagId"] == tag_id and not tag["isDelete"]:
            tag["isDelete"] = True
            tag["updatedAt"] = datetime.utcnow()
            return {"detail": "Tag deleted"}
    raise HTTPException(status_code=404, detail="Tag not found")
