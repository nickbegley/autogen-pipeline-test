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
    
    Raises:
        ValueError: If n is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be greater than 0.")

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence[:n]

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
    print_fibonacci(50)