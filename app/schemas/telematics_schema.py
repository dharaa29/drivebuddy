from pydantic import BaseModel
from datetime import datetime

class Telemetry(BaseModel):
    vehicle_id: str
    latitude: float
    longitude: float
    speed: float
    timestamp: datetime
    direction: float  # add this field
