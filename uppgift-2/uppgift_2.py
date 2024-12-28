
def sum_list(numbers: list[int]) -> int:
    """
    Returnerar summan av alla siffror i listan.
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(sum_list([1, 2, 3, 4, 5]))  # 15
