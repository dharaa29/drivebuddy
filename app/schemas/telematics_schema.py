from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Telemetry(BaseModel):
    vehicle_id: str
    latitude: float
    longitude: float
    timestamp: datetime
    speed: float
    speed_accuracy: Optional[float] = None
    accuracy: Optional[float] = None
    altitude: Optional[float] = None
    altitude_accuracy: Optional[float] = None
    heading: Optional[float] = None
    heading_accuracy: Optional[float] = None

class TelemetryRecord(Telemetry):
    record_id: str
    direction: float
