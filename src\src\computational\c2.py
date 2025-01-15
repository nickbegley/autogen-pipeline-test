"""
Monte Carlo Pi Estimation

This module provides a function to estimate the value of π (pi) using the Monte Carlo method.
The Monte Carlo method involves random sampling to obtain numerical results. In this case,
we will randomly generate points in a square and determine how many fall within a quarter circle
inscribed within that square to estimate the value of π.

Usage:
    To estimate π, call the `estimate_pi` function with the desired number of samples.
"""

import random

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random points to generate for the estimation.

    Returns:
        float: An estimate of π calculated to four significant digits.
    
    Raises:
        ValueError: If num_samples is less than or equal to zero.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")

    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)

if __name__ == "__main__":
    # Example usage
    try:
        samples = 1000000
        pi_value = estimate_pi(samples)
        print(f"Estimated π: {pi_value}")
    except ValueError as e:
        print(e)