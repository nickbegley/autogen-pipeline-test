"""
Monte Carlo Pi Estimation

This module implements the Monte Carlo method to estimate the value of π (pi)
to four significant digits. The Monte Carlo method uses random sampling to
determine the ratio of points that fall inside a quarter circle versus the
total number of points sampled.

Usage:
    To estimate π, create an instance of the MonteCarloPiEstimator and call
    the estimate_pi method.

Example:
    estimator = MonteCarloPiEstimator(num_samples=10000)
    pi_estimate = estimator.estimate_pi()
    print(f"Estimated value of π: {pi_estimate:.4f}")
"""

import random

class MonteCarloPiEstimator:
    """Class to estimate the value of π using the Monte Carlo method."""
    
    def __init__(self, num_samples: int):
        """
        Initialize the estimator with the number of samples.

        Args:
            num_samples (int): The number of random points to sample.

        Raises:
            ValueError: If num_samples is less than or equal to zero.
        """
        if num_samples <= 0:
            raise ValueError("Number of samples must be greater than zero.")
        
        self.num_samples = num_samples

    def estimate_pi(self) -> float:
        """
        Estimate the value of π using the Monte Carlo method.

        Returns:
            float: The estimated value of π rounded to four significant digits.
        """
        inside_circle = 0
        
        for _ in range(self.num_samples):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        
        pi_estimate = (inside_circle / self.num_samples) * 4
        return round(pi_estimate, 4)

# Example usage
if __name__ == "__main__":
    estimator = MonteCarloPiEstimator(num_samples=10000)
    pi_estimate = estimator.estimate_pi()
    print(f"Estimated value of π: {pi_estimate:.4f}")