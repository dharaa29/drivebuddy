from fastapi import APIRouter
from typing import List
from app.schemas.telematics_schema import Telemetry, TelemetryRecord
from app.controllers.telematics_controller import (
    create_telemetry,
    get_all_telemetry,
    get_telemetry_by_vehicle,
    update_telemetry_record,
    delete_telemetry_record
)

router = APIRouter(prefix="/telematics", tags=["Telematics"])

@router.post("/", response_model=dict)
def add_telemetry(data: Telemetry):
    return create_telemetry(data)

@router.get("/", response_model=List[TelemetryRecord])
def fetch_all_telemetry():
    return get_all_telemetry()

@router.get("/{vehicle_id}", response_model=List[TelemetryRecord])
def fetch_telemetry_by_vehicle(vehicle_id: str):
    return get_telemetry_by_vehicle(vehicle_id)

@router.put("/{record_id}", response_model=TelemetryRecord)
def modify_telemetry(record_id: str, data: Telemetry):
    return update_telemetry_record(record_id, data)

@router.delete("/{record_id}")
def remove_telemetry(record_id: str):
    return delete_telemetry_record(record_id)
