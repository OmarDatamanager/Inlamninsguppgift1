

def fibonacci(n: int) -> list[int]:
    """
    Returnerar en lista med de n första talen i Fibonacci's talföljd.
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib
    
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci(1))   # Output: [0]
print(fibonacci(0))   # Output: []
print(fibonacci(5))   # Output: [0, 1, 1, 2, 3]
    
