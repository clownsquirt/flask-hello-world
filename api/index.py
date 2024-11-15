import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load API key from environment variable
API_KEY = os.getenv("API_KEY")

@app.route('/')
def hello_world():
    # Get the API key from the request header
    key = request.headers.get("Authorization")

    # Validate the key
    if key != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Hello, World!"})

# Expose the Flask app as a module-level variable named "app"
# No need to change anything else
