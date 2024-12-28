

def multiplication_table(n: int, limet: int) -> list[int]:
    """
    Returnerar multiplikationstabellen för n upp till limit i en lista.
    """
    return [n * i for i in range(1, limet + 1)]

print(multiplication_table(2, 10))  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(multiplication_table(5, 5))   # Output: [5, 10, 15, 20, 25]
print(multiplication_table(3, 7))   # Output: [3, 6, 9, 12, 15, 18, 21]

