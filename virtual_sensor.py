import random
import time
import requests  
API_URL = "https://<your-api-id>.execute-api.us-east-1.amazonaws.com/dev/sensor"

while True:
    temperature = round(random.uniform(24.0, 32.0), 1)
    humidity = round(random.uniform(45.0, 75.0), 1)

    payload = {
        "device_id": "EnvironmentalSensor",
        "temperature": temperature,
        "humidity": humidity
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)
        print(f"Sent: Temp={temperature}°C, Humidity={humidity}% | Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to post to AWS: {e}")

    print("-" * 40)
    time.sleep(5)