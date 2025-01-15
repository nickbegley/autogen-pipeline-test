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
        ValueError: If n is not a positive integer.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be a positive integer.")
    
    fibonacci_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

def main() -> None:
    """
    Main function to generate and print the first 50 Fibonacci numbers.
    """
    fibonacci_numbers = generate_fibonacci(50)
    print(fibonacci_numbers)

if __name__ == "__main__":
    main()