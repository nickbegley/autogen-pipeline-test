"""
Monte Carlo Pi Estimation

This module implements the Monte Carlo method to estimate the value of π (Pi)
by simulating random points in a unit square and counting how many fall inside
a quarter circle inscribed within that square. The ratio of points inside the
circle to the total number of points is used to estimate π.
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
    ValueError: If num_samples is not a positive integer.
    """
    if num_samples <= 0:
        raise ValueError("num_samples must be a positive integer.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    # Example usage
    try:
        samples = 1000000
        pi_value = estimate_pi(samples)
        print(f"Estimated value of π with {samples} samples: {pi_value}")
    except ValueError as e:
        print(f"Error: {e}")