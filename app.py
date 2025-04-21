import os
import time
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Hello from Friday's brain."

@app.route("/set_alarm", methods=["GET"])
def set_alarm():
    time_str = request.args.get("time", "06:45")
    timestamp = int(time.time())  # 중복 방지를 위한 고유한 값
    full_text = f"set_alarm:=:{time_str}:{timestamp}"  # Tasker에서 뒤에 있는 값은 무시해도 됨

    print(f"[Friday] Alarm requested for: {time_str} (msg: {full_text})")

    requests.get("https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush", params={
        "apikey": "b42fb597f8604f96b8fb46375cd79b5d",
        "deviceId": "b42fb597f8604f96b8fb46375cd79b5d",
        "text": full_text
    })

    return f"Alarm set for {time_str} (sent via Join)", 200

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render는 이 환경변수로 포트를 지정함
    app.run(host="0.0.0.0", port=port, debug=True)
