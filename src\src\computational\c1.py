"""
Fibonacci Sequence Generator

This module contains a function to generate and print the first 50 Fibonacci numbers.
The Fibonacci sequence is defined as follows:
- The first two numbers in the sequence are 0 and 1.
- Each subsequent number is the sum of the two preceding ones.

Example:
    Calling the function `generate_fibonacci_sequence()` will print the first 50 Fibonacci numbers.
"""

from typing import List

def generate_fibonacci_sequence(n: int = 50) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Parameters:
        n (int): The number of Fibonacci numbers to generate. Defaults to 50.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

def print_fibonacci_sequence() -> None:
    """
    Print the first 50 Fibonacci numbers.
    """
    fibonacci_numbers = generate_fibonacci_sequence()
    print(fibonacci_numbers)

if __name__ == "__main__":
    print_fibonacci_sequence()