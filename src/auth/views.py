# src/auth/views.py
# GAP-3: No rate limiting, GAP-4: No session tokens

from flask import Flask, request, jsonify
from .models import User

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    """Register new user - GAP-2: No email validation called"""
    data = request.get_json()
    user = User(
        data.get('email'),
        data.get('password'),
        data.get('first_name', ''),
        data.get('last_name', '')
    )
    return jsonify({"status": "success", "user": user.to_dict()}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    GAP-3: No rate limiting check
    GAP-4: No session token returned
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Simulate user lookup (no database)
    user = User(email, password, "Test", "User")
    
    # GAP-3: No rate limit check before authentication
    # GAP-4: No token generation after successful login
    if user.authenticate(password):
        return jsonify({
            "status": "success",
            "message": "Login successful"
            # ❌ GAP-4: Missing "token": generate_token()
        }), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401
