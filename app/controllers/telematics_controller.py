from typing import List
from datetime import datetime
import uuid, math
from ..schemas.telematics_schema import Telemetry, TelemetryRecord
from fastapi import HTTPException

# Globals
telemetry_data: List[TelemetryRecord] = []
events = {"sudden_brake": [], "sudden_acceleration": [], "sharp_turn": []}
driver_score = 100

# Thresholds
SUDDEN_SPEED_DIFF = 15
SHARP_TURN_ANGLE = 30
MAX_GPS_ACCURACY = 50
MAX_SPEED_ACCURACY = 5

# Utility functions
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda / 2)**2
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))

def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    diff_long = math.radians(lon2 - lon1)
    x = math.sin(diff_long) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(diff_long)
    bearing = math.degrees(math.atan2(x, y))
    return (bearing + 360) % 360

# CRUD + Processing Functions
def create_telemetry(data: Telemetry):
    global driver_score
    if data.accuracy and data.accuracy > MAX_GPS_ACCURACY:
        return {"message": "Ignored due to poor GPS accuracy"}

    direction = 0
    bearing_change = 0
    distance_from_last = 0
    direction_used = False

    if telemetry_data:
        prev = telemetry_data[-1]
        distance_from_last = haversine(prev.latitude, prev.longitude, data.latitude, data.longitude)
        direction = calculate_bearing(prev.latitude, prev.longitude, data.latitude, data.longitude)
        bearing_change = abs(direction - prev.direction)
        bearing_change = min(bearing_change, 360 - bearing_change)
        direction_used = True

    record = TelemetryRecord(**data.dict(), record_id=str(uuid.uuid4()), direction=direction)
    telemetry_data.append(record)

    sudden_brake = sudden_acc = sharp_turn = False

    if len(telemetry_data) > 1:
        prev = telemetry_data[-2]
        time_diff = (data.timestamp - prev.timestamp).total_seconds()
        speed_diff = data.speed - prev.speed
        reliable_speed = data.speed_accuracy is None or data.speed_accuracy <= MAX_SPEED_ACCURACY

        if reliable_speed and speed_diff < -SUDDEN_SPEED_DIFF and time_diff <= 10:
            sudden_brake = True
            driver_score -= 5
            events["sudden_brake"].append({"latitude": data.latitude, "longitude": data.longitude,
                                           "current_speed": data.speed, "previous_speed": prev.speed,
                                           "timestamp": data.timestamp, "event_type": "SUDDEN_BRAKE"})

        if reliable_speed and speed_diff > SUDDEN_SPEED_DIFF and time_diff <= 10:
            sudden_acc = True
            driver_score -= 3
            events["sudden_acceleration"].append({"latitude": data.latitude, "longitude": data.longitude,
                                                  "current_speed": data.speed, "previous_speed": prev.speed,
                                                  "timestamp": data.timestamp, "event_type": "SUDDEN_ACCELERATION"})

        if bearing_change >= SHARP_TURN_ANGLE:
            sharp_turn = True
            driver_score -= 2
            events["sharp_turn"].append({"latitude": data.latitude, "longitude": data.longitude,
                                         "current_speed": data.speed, "previous_speed": prev.speed,
                                         "timestamp": data.timestamp, "event_type": "SHARP_TURN",
                                         "bearing_change": round(bearing_change, 2)})

    return {
        "message": "Telemetry processed successfully",
        "record": record,
        "sudden_brake": sudden_brake,
        "sudden_acceleration": sudden_acc,
        "sharp_turn": sharp_turn,
        "driver_score": driver_score,
        "event_details": events
    }

def get_all_telemetry():
    return telemetry_data

def get_telemetry_by_vehicle(vehicle_id: str):
    results = [t for t in telemetry_data if t.vehicle_id == vehicle_id]
    if not results:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return results

def update_telemetry_record(record_id: str, data: Telemetry):
    for idx, t in enumerate(telemetry_data):
        if t.record_id == record_id:
            updated = TelemetryRecord(**data.dict(), record_id=record_id, direction=t.direction)
            telemetry_data[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Record not found")

def delete_telemetry_record(record_id: str):
    global telemetry_data
    for idx, t in enumerate(telemetry_data):
        if t.record_id == record_id:
            telemetry_data.pop(idx)
            return {"message": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Record not found")

