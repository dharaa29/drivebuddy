from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
import uuid
from app.enums.status_enum import Status
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

# In-memory storage
categories_db: List[CategoryResponse] = []

# -------- GET ALL --------
@router.get("/", response_model=List[CategoryResponse])
def get_all_categories():
    return [cat for cat in categories_db if not cat.isDelete]

# -------- GET BY ID --------
@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: str):
    for cat in categories_db:
        if cat.categoryId == category_id and not cat.isDelete:
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

# -------- CREATE --------
@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate):
    new_category = CategoryResponse(
        categoryId=str(uuid.uuid4()),
        name=category.name,
        description=category.description,
        slug=category.slug,
        status=category.status,
        isDelete=False,
        createdBy=category.createdBy,
        updatedBy=None,
        createdAt=datetime.utcnow(),
        updatedAt=None
    )
    categories_db.append(new_category)
    return new_category

# -------- UPDATE --------
@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: str, category_update: CategoryUpdate):
    for cat in categories_db:
        if cat.categoryId == category_id and not cat.isDelete:
            if category_update.name: cat.name = category_update.name
            if category_update.description: cat.description = category_update.description
            if category_update.slug: cat.slug = category_update.slug
            if category_update.status: cat.status = category_update.status
            cat.updatedBy = category_update.updatedBy
            cat.updatedAt = datetime.utcnow()
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

# -------- DELETE --------
@router.delete("/{category_id}")
def delete_category(category_id: str):
    for cat in categories_db:
        if cat.categoryId == category_id and not cat.isDelete:
            cat.isDelete = True
            cat.updatedAt = datetime.utcnow()
            return {"detail": "Category deleted successfully"}
    raise HTTPException(status_code=404, detail="Category not found")
