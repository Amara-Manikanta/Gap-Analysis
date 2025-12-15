# src/payment/views.py
# GAP-6: Broad exception handling exposes errors

from flask import Flask, request, jsonify
from .models import Payment

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def process_payment():
    """Process payment - GAP-6: Exposes internal errors"""
    data = request.get_json()
    
    try:
        payment = Payment(
            data['card_number'],
            data['cvv'],
            data['expiry'],
            data['amount']
        )
        
        result = payment.process()
        return jsonify(result), 200
        
    except KeyError as e:
        # ❌ GAP-6: Generic error response
        return jsonify({"status": "error", "message": f"Missing {e.args[0]}"}), 400
        
    except Exception as e:
        # ❌ GAP-6: Exposes full error details to client
        return jsonify({
            "status": "error",
            "message": str(e),
            "error_type": type(e).__name__  # SECURITY ISSUE
        }), 500
