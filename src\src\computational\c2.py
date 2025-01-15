"""
Monte Carlo Pi Estimation

This module contains a function to estimate the value of π using the Monte Carlo method.
The estimation is based on randomly generating points in a square that encompasses a quarter circle.
The ratio of points inside the quarter circle to the total points generated is used to estimate π.
"""

import random

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random points to generate for the estimation.

    Returns:
        float: An estimate of π rounded to four significant digits.

    Raises:
        ValueError: If num_samples is not a positive integer.
    """
    if num_samples <= 0:
        raise ValueError("num_samples must be a positive integer.")

    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)

# Example usage
if __name__ == "__main__":
    samples = 1000000
    pi_value = estimate_pi(samples)
    print(f"Estimated value of π: {pi_value}")