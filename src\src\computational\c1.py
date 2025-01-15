"""
Fibonacci Sequence Generator

This module provides a function to generate and print the first 50
numbers in the Fibonacci sequence.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    List[int]: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to print.
    """
    fibonacci_numbers = generate_fibonacci(n)
    print("First", n, "Fibonacci numbers:", fibonacci_numbers)

if __name__ == "__main__":
    print_fibonacci(50)