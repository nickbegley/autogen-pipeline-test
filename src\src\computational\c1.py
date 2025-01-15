# src/computational/c1.py

"""
Fibonacci Sequence Generator

This module provides a function to generate and print the first 50 numbers
in the Fibonacci sequence. The Fibonacci sequence is a series of numbers
where each number is the sum of the two preceding ones, usually starting
with 0 and 1.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate a list of the first n Fibonacci numbers.

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
        next_fib = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fib)

    return fibonacci_sequence

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to print.
    """
    fib_sequence = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fib_sequence}")

if __name__ == "__main__":
    print_fibonacci(50)