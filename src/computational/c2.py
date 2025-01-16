"""
Monte Carlo Pi Estimation Module

This module implements a Monte Carlo method to estimate the value of π (pi).
The estimation is performed by randomly generating points in a unit square and
calculating the ratio of points that fall inside a quarter circle to the total
number of points. The result is scaled to estimate π.
"""

import random


def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random points to generate for the estimation.

    Returns:
        float: The estimated value of π, rounded to four significant digits.

    Raises:
        ValueError: If num_samples is less than or equal to zero.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")

    points_inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    pi_estimate = (points_inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    # Example usage
    num_samples = 1000000
    pi_value = estimate_pi(num_samples)
    print(f"Estimated value of π with {num_samples} samples: {pi_value}")