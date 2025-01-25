"""
Monte Carlo Pi Estimation

This module provides a function to estimate the value of π using the Monte Carlo
method. The estimation is based on generating random points in a unit square and
counting how many fall within the quarter circle inscribed within that square.
The result is returned to four significant digits.
"""

import random

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Parameters:
    num_samples (int): The number of random points to generate.

    Returns:
    float: The estimated value of π rounded to four significant digits.

    Raises:
    ValueError: If num_samples is less than or equal to zero.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x ** 2 + y ** 2) <= 1:
            inside_circle += 1

    pi_estimate = (4 * inside_circle) / num_samples
    return round(pi_estimate, 4)

if __name__ == "__main__":
    # Example usage
    num_samples = 10000
    pi_value = estimate_pi(num_samples)
    print(f"Estimated value of π with {num_samples} samples: {pi_value}")