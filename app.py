import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Hello from Friday's brain."

@app.route("/set_alarm", methods=["GET"])
def set_alarm():
    time = request.args.get("time", "06:45")
    print(f"[Friday] Alarm requested for: {time}")

    # Join API 호출
    requests.get("https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush", params={
        "apikey": "b42fb597f8604f96b8fb46375cd79b5d",
        "deviceId": "b42fb597f8604f96b8fb46375cd79b5d",
        "text": f"set_alarm:=:{time}"
    })

    return f"Alarm set for {time} (sent via Join)", 200

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
