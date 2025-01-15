"""
Monte Carlo Pi Estimation

This module implements a Monte Carlo method to estimate the value of π (Pi).
The estimation is done by randomly generating points in a unit square and
calculating the ratio of points that fall inside a quarter circle to the total
number of points.
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
        raise ValueError("Number of samples must be a positive integer.")

    points_inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / num_samples
    return round(pi_estimate, 4)


if __name__ == "__main__":
    # Example usage
    try:
        num_samples = 1000000  # Number of samples for estimation
        pi_value = estimate_pi(num_samples)
        print(f"Estimated value of π: {pi_value}")
    except ValueError as e:
        print(e)