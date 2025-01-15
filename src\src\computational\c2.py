"""
Monte Carlo π Estimation

This module provides a function to estimate the value of π using the Monte Carlo method.
The estimation is done by randomly generating points in a square that bounds a quarter circle
and calculating the ratio of points that fall inside the quarter circle to the total number of points.
"""

import random


def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random samples to generate for the estimation.

    Returns:
        float: The estimated value of π rounded to 4 significant digits.

    Raises:
        ValueError: If num_samples is less than or equal to 0.
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
    # Example usage
    try:
        num_samples = 1000000
        pi_value = estimate_pi(num_samples)
        print(f"Estimated value of π: {pi_value}")
    except ValueError as e:
        print(e)