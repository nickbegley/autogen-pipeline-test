"""
Fibonacci Sequence Generator

This module contains a function to generate and print the first 50 Fibonacci numbers.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
usually starting with 0 and 1.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate a list containing the first n Fibonacci numbers.
    
    Parameters:
    n (int): The number of Fibonacci numbers to generate. Must be a positive integer.

    Returns:
    List[int]: A list of the first n Fibonacci numbers.
    
    Raises:
    ValueError: If n is not a positive integer.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be a positive integer.")
    
    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_fib = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fib)

    return fibonacci_sequence[:n]

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers to the console.
    
    Parameters:
    n (int): The number of Fibonacci numbers to print. Must be a positive integer.
    
    Raises:
    ValueError: If n is not a positive integer.
    """
    fibonacci_numbers = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

if __name__ == "__main__":
    print_fibonacci(50)