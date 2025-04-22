import requests
import time
from flask import Flask, request

app = Flask(__name__)

# Pushbullet 토큰 (주의: 노출 금지)
PUSHBULLET_TOKEN = "o.SDSws2OBVRRZcYqiz3fye9BTKcWrmt1V"  # 여기에 본인 토큰 입력

def send_pushbullet_note(title, body):
    response = requests.post(
        "https://api.pushbullet.com/v2/pushes",
        json={"type": "note", "title": title, "body": body},
        headers={"Access-Token": PUSHBULLET_TOKEN}
    )
    print(f"[Friday] Pushbullet response: {response.status_code}, {response.text}")
    return response

@app.route("/")
def home():
    return "👋 Hello from Friday's brain."

@app.route("/set_alarm", methods=["GET"])
def set_alarm():
    time_str = request.args.get("time", "06:45")
    timestamp = int(time.time())
    full_text = f"set_alarm:=:{time_str}:{timestamp}"

    print(f"[Friday] Alarm requested for: {time_str} (msg: {full_text})")
    send_pushbullet_note("Friday", full_text)

    return f"Alarm set for {time_str} (sent via Pushbullet)", 200

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
