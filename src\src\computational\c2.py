"""
Monte Carlo Pi Estimation

This module contains a function to estimate the value of π using the Monte Carlo method.
The estimation is based on the ratio of points that fall inside a quarter circle to the total number of points.
"""

import random

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random samples to use for the estimation.

    Returns:
        float: The estimated value of π rounded to four significant digits.

    Raises:
        ValueError: If num_samples is not a positive integer.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be a positive integer.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    # Example usage: Estimate π with 100,000 samples
    samples = 100000
    pi_value = estimate_pi(samples)
    print(f"Estimated value of π with {samples} samples: {pi_value}")