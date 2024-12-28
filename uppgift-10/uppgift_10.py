
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Konverterar en temperatur från Celsius till Fahrenheit.
    """
    return celsius * 9/5 + 32

print(celsius_to_fahrenheit(0))    # Output: 32.0
print(celsius_to_fahrenheit(100))  # Output: 212.0
print(celsius_to_fahrenheit(-40))  # Output: -40.0
print(celsius_to_fahrenheit(37))   # Output: 98.6

