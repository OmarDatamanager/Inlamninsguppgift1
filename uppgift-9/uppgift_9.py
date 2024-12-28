
def is_palindrome(string: str) -> bool:
    """
    Kontrollerar om en given sträng är ett palindrom.
    """
    cleand_string = ''.join([char.lower() for char in string if char.isalnum()])
    return cleand_string == cleand_string[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("Hello"))                           # Output: False
print(is_palindrome("Madam"))                           # Output: True


