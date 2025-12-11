import requests
import time
from datetime import datetime, timezone
import random

# Replace with your FastAPI endpoint (ngrok or localhost)
API_URL = "https://widowly-conception-runnier.ngrok-free.dev/telematics/"

# Vehicle ID for this simulator
VEHICLE_ID = "vehicle_001"

# Example route points (latitude, longitude)
route = [
    (12.971293, 77.594704),
    (12.972000, 77.595000),
    (12.973000, 77.596000),
    (12.974000, 77.597000),
]

# Function to simulate speed (km/h)
def simulate_speed():
    return round(random.uniform(40, 120), 2)

# Send telematics point to API
def send_point(lat, lon, speed):
    timestamp = datetime.now(timezone.utc).isoformat()
    point = {
        "vehicle_id": VEHICLE_ID,   # Required field!
        "latitude": round(lat, 6),
        "longitude": round(lon, 6),
        "speed": speed,
        "timestamp": timestamp
    }
    try:
        response = requests.post(API_URL, json=point)
        print(f"Sent: {point} | Status: {response.status_code}")
    except Exception as e:
        print("Error sending point:", e)

# Simulate trip
for lat, lon in route:
    speed = simulate_speed()
    send_point(lat, lon, speed)
    time.sleep(1)  # wait 1 sec between points
