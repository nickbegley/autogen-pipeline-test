"""
This module implements the Monte Carlo method to estimate the value of π (Pi).
The estimation is done by simulating random points in a square that bounds a quarter circle
and calculating the ratio of points that fall within the quarter circle to the total number of points.

The final estimate of π is obtained by multiplying this ratio by 4.
"""

import random


def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Parameters:
        num_samples (int): The number of random points to sample.

    Returns:
        float: The estimated value of π rounded to 4 significant digits.

    Raises:
        ValueError: If num_samples is not a positive integer.
    """
    if num_samples <= 0:
        raise ValueError("The number of samples must be a positive integer.")

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
    num_samples = 1000000
    pi_value = estimate_pi(num_samples)
    print(f"Estimated value of π with {num_samples} samples: {pi_value}")