import secrets

# Generate a secure API key
api_key = secrets.token_hex(32)
print(f"Your API Key: {api_key}")