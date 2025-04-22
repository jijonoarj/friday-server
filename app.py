import requests
import time
from flask import Flask, request

app = Flask(__name__)

# Your actual Pushbullet token
PUSHBULLET_TOKEN = "o.SDSws2OBVRRZcYqiz3fye9BTKcWrmt1V"

@app.route("/")
def home():
    return "👋 Hello from Friday's brain."

@app.route("/command", methods=["GET"])
def command():
    text = request.args.get("text", "noop:=:missing_command")
    timestamp = int(time.time())
    full_text = f"{text}:{timestamp}"  # Add timestamp to ensure uniqueness

    print(f"[Friday] Command requested: {full_text}")

    # Send to Pushbullet
    requests.post(
        "https://api.pushbullet.com/v2/pushes",
        headers={
            "Access-Token": PUSHBULLET_TOKEN,
            "Content-Type": "application/json"
        },
        json={
            "type": "note",
            "title": "Friday",
            "body": full_text
        }
    )

    return f"Command sent: {full_text}", 200

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0)
