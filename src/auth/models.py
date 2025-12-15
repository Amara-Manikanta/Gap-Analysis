# src/auth/models.py
# GAP-1: Passwords stored in PLAIN TEXT (should use bcrypt)

from datetime import datetime

class User:
    """User model for authentication"""
    
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password  # ❌ GAP-1: Plain text (should be bcrypt)
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.is_active = True
    
    def authenticate(self, password):
        """Verify password - GAP-1: Direct comparison"""
        return self.password == password  # ❌ No bcrypt verification
    
    def to_dict(self):
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active
        }
