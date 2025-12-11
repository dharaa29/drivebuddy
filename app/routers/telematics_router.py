from fastapi import APIRouter
from app.schemas.telematics_schema import TelematicsCreate
from ..controllers.telematics_controller import create_telematics, get_all_telematics

router = APIRouter(prefix="/telematics", tags=["Telematics"])

@router.post("/", response_model=str)
def add_telematics(data: TelematicsCreate):
    return create_telematics(data)

@router.get("/", response_model=list)
def fetch_telematics():
    return get_all_telematics()


