from pydantic import BaseModel, Field
from datetime import datetime

class Telematics(BaseModel):
    latitude: float = Field(..., example=12.9716)
    longitude: float = Field(..., example=77.5946)
    speed: float = Field(..., example=60.5)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
