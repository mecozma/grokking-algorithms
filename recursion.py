"""Recursion."""

def print_factorial(number):
    # Base case.
    if number == 1:
        return 1
    # Recursive case.
    else:
        return number * print_factorial(number - 1)


print(print_factorial(5))
