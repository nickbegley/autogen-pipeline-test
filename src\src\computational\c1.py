"""
Fibonacci Sequence Generator

This module provides a function to generate and print the first 50 Fibonacci numbers.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
usually starting with 0 and 1.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.

    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer greater than 0.")
    
    fibonacci_numbers = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b  # Update to the next Fibonacci numbers

    return fibonacci_numbers

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fibonacci_numbers = generate_fibonacci(n)
    for number in fibonacci_numbers:
        print(number)

if __name__ == "__main__":
    # Generate and print the first 50 Fibonacci numbers
    print_fibonacci(50)