# src/utils/validators.py
# GAP-2: Email regex too restrictive

import re

def validate_email(email):
    """
    GAP-2: Incomplete RFC 5322 validation
    Rejects valid emails like "user.name@domain.co.uk"
    Accepts invalid like "user@domain.c"
    """
    # ❌ GAP-2: Too simple regex
    pattern = r'^[a-z]+@[a-z]+\.[a-z]+$'
    return bool(re.match(pattern, email, re.IGNORECASE))

def validate_password(password):
    """Basic password validation"""
    return len(password) >= 8
