# src/utils/security.py
# GAP-3: Rate limiter always allows, GAP-4: Token stub

import time
import secrets

class RateLimiter:
    """GAP-3: Always returns True - no actual limiting"""
    
    def is_allowed(self, ip_address):
        """
        GAP-3: No real rate limiting (should track 5/min per IP)
        """
        # ❌ GAP-3: Always allows unlimited attempts
        return True

class TokenManager:
    """GAP-4: Token generation exists but never called"""
    
    def generate_token(self, user_id):
        """
        GAP-4: Defined but never used in login endpoint
        """
        return secrets.token_urlsafe(32)
    
    def validate_token(self, token):
        """Stub validation"""
        return True
