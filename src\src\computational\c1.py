# src/computational/c1.py

from typing import List

def fibonacci_sequence(n: int) -> List[int]:
    """Generate the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        List[int]: A list containing the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is non-positive.
    """
    if n <= 0:
        raise ValueError("The number of Fibonacci numbers to generate must be positive.")

    fib_sequence = [0, 1]

    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence[:n]


def print_fibonacci(n: int) -> None:
    """Print the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    fib_sequence = fibonacci_sequence(n)
    print(f"The first {n} Fibonacci numbers are: {fib_sequence}")


if __name__ == "__main__":
    print_fibonacci(50)