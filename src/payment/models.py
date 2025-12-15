# src/payment/models.py
# GAP-5: No Luhn algorithm implementation

class Payment:
    """Payment model"""
    
    def __init__(self, card_number, cvv, expiry, amount):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry  # MM/YY format
        self.amount = amount
    
    def validate_card(self):
        """
        GAP-5: No Luhn validation - accepts invalid cards
        Should implement Luhn algorithm
        """
        # ❌ GAP-5: Only length check, no Luhn checksum
        cleaned = ''.join(c for c in self.card_number if c.isdigit())
        return len(cleaned) >= 13  # Accepts ANY 13+ digit number
    
    def process(self):
        if self.validate_card():
            return {"status": "success"}
        return {"status": "failed"}
