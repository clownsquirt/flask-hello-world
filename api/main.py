from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your generated API key
API_KEY = "637f75dc673a97611070da17c74fc8cef3cdbb4efc95ec56e1df8e45065ebfec"

@app.route('/')
def hello_world():
    # Get the API key from the request header
    key = request.headers.get("Authorization")
    
    # Validate the key
    if key != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run()
