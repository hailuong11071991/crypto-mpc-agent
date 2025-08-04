from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle():
    data = request.get_json()
    user_input = data.get("prompt", "")

    if "btc" in user_input.lower():
        return jsonify({"response": "📈 BTC hiện đang tăng"})
    elif "eth" in user_input.lower():
        return jsonify({"response": "📉 ETH đang điều chỉnh nhẹ"})
    else:
        return jsonify({"response": f"Bạn vừa nhập: {user_input}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
