
def word_count(text: str) -> int:
    """
    Returnerar antalet ord i en given text.
    """
    words = text.split()
    return len(words)

print(word_count("This is a simple test."))  # Output: 5
print(word_count("Another example with more words in the sentence."))  # Output: 8
print(word_count(""))  # Output: 0
print(word_count("Python programming is fun!"))  # Output: 4

