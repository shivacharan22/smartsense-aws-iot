import json
import time

def lambda_handler(event, context=None):
    # Set CORS headers so your web frontend can call the API
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    try:
        # Handle API Gateway proxy payload (comes as a JSON string under "body")
        if "body" in event and event["body"]:
            body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
        else:
            body = event  # Direct Lambda console test payload

        device_id = body.get("device_id", "EnvironmentalSensor")
        temperature = float(body.get("temperature", 0.0))
        humidity = float(body.get("humidity", 0.0))

        item = {
            "device_id": device_id,
            "timestamp": int(time.time()),
            "temperature": temperature,
            "humidity": humidity
        }

        print("Data processed successfully:", json.dumps(item))

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "message": "Environmental data processed successfully",
                "data": item
            })
        }

    except Exception as error:
        print("Error:", str(error))
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({
                "message": "Error processing data",
                "error": str(error)
            })
        }