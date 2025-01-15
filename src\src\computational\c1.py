"""
Fibonacci Sequence Generator

This module provides a function to generate and print the first 50 Fibonacci numbers.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be a positive integer.")
    
    fibonacci_numbers = [0, 1]
    
    for _ in range(2, n):
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fib)

    return fibonacci_numbers[:n]

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fibonacci_sequence = generate_fibonacci(n)
    print(f"First {n} Fibonacci numbers: {fibonacci_sequence}")

if __name__ == "__main__":
    print_fibonacci(50)