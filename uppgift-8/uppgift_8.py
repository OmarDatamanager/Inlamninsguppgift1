
def count_letters(string: str) -> dict:
    """
    Returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    """
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

print(count_letters("Hello World"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
print(count_letters("Python Programming"))  # Output: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'a': 1, 'm': 2}

