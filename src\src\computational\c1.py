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
        raise ValueError("Input must be a positive integer greater than 0.")
    
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    
    return fibonacci_numbers[:n]

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.

    Raises:
        ValueError: If n is less than 1.
    """
    fibonacci_numbers = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

if __name__ == "__main__":
    print_fibonacci(50)