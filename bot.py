import os
from flask import Flask, request
import requests

TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        # Simple reply logic:
        reply = f"Your message was: {text}"
        
        payload = {"chat_id": chat_id, "text": reply}
        requests.post(TELEGRAM_URL, json=payload)

    return "OK"
