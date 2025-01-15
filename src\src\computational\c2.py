"""
Monte Carlo Pi Estimation

This module provides a function to estimate the value of π using the
Monte Carlo method. The estimation is based on random sampling within a
unit square that circumscribes a quarter circle. The ratio of points
inside the quarter circle to the total points sampled is used to
estimate π.

Functions:
- estimate_pi(num_samples: int) -> float: Estimates the value of π
  using the specified number of random samples.
"""

import random


def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Parameters:
    - num_samples (int): The number of random points to sample.

    Returns:
    - float: An estimate of π rounded to 4 significant digits.

    Raises:
    - ValueError: If num_samples is less than or equal to zero.
    """
    if num_samples <= 0:
        raise ValueError("num_samples must be greater than zero.")

    points_inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x ** 2 + y ** 2 <= 1:
            points_inside_circle += 1

    # Estimate π
    pi_estimate = (points_inside_circle / num_samples) * 4
    return round(pi_estimate, 4)


if __name__ == "__main__":
    try:
        samples = 1000000  # Example usage with 1 million samples
        pi_value = estimate_pi(samples)
        print(f"Estimated value of π: {pi_value}")
    except ValueError as e:
        print(f"Error: {e}")