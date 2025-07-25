__all__ = ['validate_password']
def validate_password(password):
    """Validates the password based on specific criteria."""
    if len(password) < 6 or len(password) > 16:
        return False, "Password must be between 6 and 16 characters long."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is valid."