# src/computational/c1.py

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    List[int]: A list containing the first n Fibonacci numbers.
    
    Raises:
    ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("The number of Fibonacci numbers to generate must be at least 1.")

    fibonacci_sequence = [0, 1]
    
    for i in range(2, n):
        next_fib = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fib)

    return fibonacci_sequence[:n]

def print_fibonacci(n: int) -> None:
    """
    Print the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to print.
    """
    fibonacci_numbers = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

if __name__ == "__main__":
    print_fibonacci(50)