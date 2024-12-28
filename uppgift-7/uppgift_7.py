
def validate_password(password: str) -> bool:
    """
    Kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    """
    if len(password) < 8:
        return False

    for char in password:
        if char.isdigit():
            return True

    return False

print(validate_password("password1"))  # Output: True
print(validate_password("pass"))       # Output: False
print(validate_password("password"))   # Output: False
print(validate_password("pass1234"))   # Output: True

