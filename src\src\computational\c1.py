"""
Fibonacci Sequence Generator

This module contains a function to generate and print the first 50 Fibonacci numbers.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []

    fibonacci_sequence = [0, 1]
    
    for _ in range(2, n):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)

    return fibonacci_sequence[:n]

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fibonacci_numbers = generate_fibonacci(n)
    print("Fibonacci Sequence:")
    for number in fibonacci_numbers:
        print(number)

if __name__ == "__main__":
    print_fibonacci(50)