from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, threaded=False)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.data.decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Unsupported Media Type", 415

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Your English Academy bot is live! 🎉")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

