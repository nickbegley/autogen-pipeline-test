"""
Monte Carlo Pi Estimation

This module implements a Monte Carlo method to estimate the value of π (pi)
to four significant digits. The estimation is based on random sampling within
a square that encloses a quarter circle.
"""

import random


def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random points to sample.

    Returns:
        float: The estimated value of π rounded to four significant digits.

    Raises:
        ValueError: If num_samples is less than or equal to zero.
    """
    if num_samples <= 0:
        raise ValueError("num_samples must be greater than zero.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    # Example usage:
    try:
        num_samples = 1000000
        pi_value = estimate_pi(num_samples)
        print(f"Estimated value of π: {pi_value}")
    except ValueError as e:
        print(f"Error: {e}")