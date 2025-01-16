"""
Monte Carlo Pi Estimation

This module implements a Monte Carlo method to estimate the value of π (Pi).
The estimation is performed by randomly sampling points in a unit square and
checking how many fall inside a quarter circle inscribed within that square.
The ratio of points inside the circle to the total number of points is used to
estimate π.

Usage:
    To use the function, call `estimate_pi(num_samples: int) -> float` with the desired
    number of random samples.
"""

import random

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Parameters:
        num_samples (int): The number of random samples to draw.

    Returns:
        float: The estimated value of π rounded to 4 significant digits.
    
    Raises:
        ValueError: If num_samples is less than or equal to zero.
    """
    if num_samples <= 0:
        raise ValueError("The number of samples must be greater than zero.")

    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return round(pi_estimate, 4)

# Example of calling the function
if __name__ == "__main__":
    num_samples = 1000000
    pi_value = estimate_pi(num_samples)
    print(f"Estimated value of π: {pi_value}")