import re
from email_validator import validate_email as validate_email_format, EmailNotValidError

def validate_password(password):
    """
    Validate password strength
    Returns tuple (is_valid, message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must include at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must include at least one lowercase letter"
    
    if not re.search(r"\d", password):
        return False, "Password must include at least one number"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must include at least one special character"
    
    return True, "Password is valid"

def validate_email(email):
    """
    Validate email format
    Returns bool
    """
    try:
        validate_email_format(email)
        return True
    except EmailNotValidError:
        return False