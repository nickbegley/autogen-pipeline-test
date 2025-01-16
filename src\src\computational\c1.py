"""
Fibonacci Sequence Generator

This module provides a function to generate and print the first 50
numbers in the Fibonacci sequence. The Fibonacci sequence is a series
of numbers in which each number (after the first two) is the sum of the
two preceding ones, typically starting with 0 and 1.
"""

from typing import List

def generate_fibonacci(n: int = 50) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate. Default is 50.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be positive.")
    
    fibonacci_numbers = [0, 1]
    
    for i in range(2, n):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_number)
    
    return fibonacci_numbers[:n]

def print_fibonacci(n: int = 50) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print. Default is 50.
    """
    fib_numbers = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fib_numbers}")

if __name__ == "__main__":
    print_fibonacci()