from flask import Flask, request, jsonify
from flask_cors import CORS
import os, requests

app = Flask(__name__)
CORS(app)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage" if BOT_TOKEN else ""

def reply_telegram(chat_id, text):
    if not BOT_TOKEN: return
    try:
        requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": text}, timeout=10)
    except Exception as e:
        print(e)

@app.route('/')
def home():
    return "Rednet-Brain LIVE 24/7 🔥"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get('message','')
    if 'hi' in msg.lower():
        reply = "Yo bro! RedNet is LIVE 24/7! 🚀 How can I help?"
    else:
        reply = f"You said: {msg} — RedNet Brain responding! 🔥"
    return jsonify({"reply": reply})

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge','OK')
    
    data = request.get_json()
    print(data)
    
    # TELEGRAM REPLY LOGIC
    if data and "message" in data and "chat" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text","")
        t = text.lower()
        
        if "hii" in t or t == "hi" or "hello" in t:
            ans = "Yoooo! I'm BACK! 🔥 REDnet LIVE 24/7 bro! What's good? 😊"
        elif "rednet" in t:
            ans = "🔥 Yeah that's me! I'm REDNET, your friendly AI! Always here to chat! 🚀"
        else:
            ans = f"You said: {text} — REDNET replying LIVE! 🚀"
        
        reply_telegram(chat_id, ans)
    
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
