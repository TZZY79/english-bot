import os
from flask import Flask, request
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# --- Webhook Handler ---
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_data = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "OK", 200

# --- Basic Commands ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Your bot is running successfully 😄")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "You said: " + message.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
