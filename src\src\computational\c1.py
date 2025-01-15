"""
Fibonacci Sequence Generator

This module defines a function to generate and print the first 50 Fibonacci numbers.
"""

def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list[int]: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence

def print_fibonacci_sequence(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fib_sequence = fibonacci_sequence(n)
    print(f"First {n} Fibonacci numbers: {fib_sequence}")

if __name__ == "__main__":
    print_fibonacci_sequence(50)