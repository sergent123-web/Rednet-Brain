from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Rednet-Brain is LIVE 24/7 🔥"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', 'OK')
    data = request.get_json()
    print(data)
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
