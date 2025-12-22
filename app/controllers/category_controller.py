from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import uuid

from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
from app.models.category_model import category_model

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

# In-memory storage
categories: List[dict] = []

# -------- GET ALL --------
@router.get("/", response_model=List[CategoryResponse])
def get_all_categories():
    return categories

# -------- GET BY ID --------
@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: str):
    for cat in categories:
        if cat["categoryId"] == category_id and not cat["isDelete"]:
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

# -------- CREATE --------
@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate):
    new_category = category_model({
        "categoryId": str(uuid.uuid4()),
        **category.dict()
    })
    categories.append(new_category)
    return new_category

# -------- UPDATE --------
@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: str, category_update: CategoryUpdate):
    for idx, cat in enumerate(categories):
        if cat["categoryId"] == category_id and not cat["isDelete"]:
            updated_cat = cat.copy()
            updated_data = category_update.dict(exclude_unset=True)
            updated_cat.update(updated_data)
            updated_cat["updatedAt"] = datetime.utcnow()
            categories[idx] = updated_cat
            return updated_cat
    raise HTTPException(status_code=404, detail="Category not found")

# -------- DELETE --------
@router.delete("/{category_id}")
def delete_category(category_id: str):
    for cat in categories:
        if cat["categoryId"] == category_id and not cat["isDelete"]:
            cat["isDelete"] = True
            cat["updatedAt"] = datetime.utcnow()
            return {"detail": "Category deleted"}
    raise HTTPException(status_code=404, detail="Category not found")
