"""
Monte Carlo Pi Estimation

This module contains a function to estimate the value of π using the Monte Carlo method.
The estimation is achieved by generating random points in a unit square and determining how many fall within a quarter circle inscribed within that square. The ratio of points inside the circle to the total number of points allows us to estimate π.

Functions:
- estimate_pi(num_samples: int) -> float: Estimates the value of π based on the number of random samples provided.
"""

import random
import math


def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random points to generate for the estimation.

    Returns:
        float: The estimated value of π rounded to four significant digits.

    Raises:
        ValueError: If num_samples is not a positive integer.
    """
    if num_samples <= 0:
        raise ValueError("The number of samples must be a positive integer.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    # Example of running the estimation
    try:
        samples = 1000000  # Number of samples for estimation
        pi_value = estimate_pi(samples)
        print(f"Estimated value of π with {samples} samples: {pi_value}")
    except ValueError as e:
        print(e)