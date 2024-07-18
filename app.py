from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/hello-world')
def home():
    return "Hello, World!"

@app.route('/webhook', methods=['POST'])
def handle_deal_created():
    try:
        data = request.json
        print(data)
        return jsonify({"status": "success", "data_received": data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
