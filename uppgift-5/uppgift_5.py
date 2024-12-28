

def filter_odd(numbers):
    """
    Denna funktion tar en lista med siffror och returnerar en ny lista som innehåller endast jämna tal.
    """
    return [number for number in numbers if number % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter_odd(numbers)
print(result)

