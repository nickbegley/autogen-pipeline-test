"""
Monte Carlo Pi Estimation

This module implements the Monte Carlo method to estimate the value of π
to four significant digits. The method relies on random sampling of points
within a unit square and calculating the ratio of points that fall within
a quarter circle inscribed within that square.
"""

import random

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random samples to generate.

    Returns:
        float: An estimate of π rounded to four significant digits.

    Raises:
        ValueError: If num_samples is less than or equal to 0.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    num_samples = 1000000  # You can adjust the number of samples
    pi_value = estimate_pi(num_samples)
    print(f"Estimated value of π: {pi_value}")