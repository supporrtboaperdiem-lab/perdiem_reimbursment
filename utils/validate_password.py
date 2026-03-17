import re

def validate_password(password: str):
    """
    Returns a list of ALL password validation errors.
    """

    errors = []

    if len(password) < 8:
        errors.append("• At least 8 characters")

    if not re.search(r"[A-Z]", password):
        errors.append("• At least one uppercase letter")

    if not re.search(r"[a-z]", password):
        errors.append("• At least one lowercase letter")

    if not re.search(r"[0-9]", password):
        errors.append("• At least one number")

    if not re.search(r"[^A-Za-z0-9]", password):
        errors.append("• At least one special character")

    return errors  # returns [] if valid