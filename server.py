from flask import Flask, request
import json
from main import execute_trade   # ⭐ connect main.py
import os
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.get_json(force=True)

    print("\n=========== ALERT RECEIVED ===========")
    print(data)

    side = data.get("side")

    if side in ["buy", "sell"]:
        execute_trade(side)

    return "OK", 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)