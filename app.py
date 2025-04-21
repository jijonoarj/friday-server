import os
import time
import logging
import requests
from flask import Flask, request

# Render 로그 출력 가능하게 설정
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Hello from Friday's brain."

@app.route("/set_alarm", methods=["GET"])
def set_alarm():
    time_str = request.args.get("time", "06:45")
    timestamp = int(time.time())  # 중복 방지용 고유 값
    full_text = f"set_alarm:=:{time_str}:{timestamp}"

    logging.info(f"[Friday] Alarm requested for: {time_str} (msg: {full_text})")

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
    port = int(os.environ.get("PORT", 10000))  # Render가 할당한 포트 사용
    app.run(host="0.0.0.0", port=port, debug=True)
