"""
Module for generating Fibonacci numbers.

This module contains a function to generate and print the first 50 Fibonacci numbers.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate a list containing the first n Fibonacci numbers.

    Args:
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

    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    
    return fibonacci_numbers

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fibonacci_numbers = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

if __name__ == "__main__":
    print_fibonacci(50)