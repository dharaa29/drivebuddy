from fastapi import APIRouter, HTTPException
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
from app.controllers.category_controller import (
    create_category,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse)
def create(payload: CategoryCreate):
    category = create_category(payload.dict())
    return category  # directly return the dict


@router.get("/", response_model=list[CategoryResponse])
def get_all():
    return get_all_categories()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_by_id(category_id: str):
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/{category_id}", response_model=dict)
def update(category_id: str, payload: CategoryUpdate):
    updated = update_category(category_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category updated successfully"}


@router.delete("/{category_id}", response_model=dict)
def delete(category_id: str, updatedBy: str):
    deleted = delete_category(category_id, updatedBy)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
