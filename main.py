from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Rednet-Brain is LIVE 24/7 🔥"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get('message','').lower()
    if 'hi' in msg:
        reply = "Yo bro! RedNet is LIVE 24/7! 🚀 How can I help?"
    else:
        reply = f"You said: {data.get('message')} — RedNet Brain responding! 🔥"
    return jsonify({"reply": reply})

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge','OK')
    print(request.get_json())
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
