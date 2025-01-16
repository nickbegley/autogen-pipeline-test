"""
Module for estimating π using the Monte Carlo method and visualizing the convergence of the estimation.

This module contains functions to perform the Monte Carlo simulation for π estimation
and to visualize the results using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Args:
        num_samples (int): The number of random samples to generate.

    Returns:
        float: The estimated value of π based on the random samples.
    """
    inside_circle = 0

    for _ in range(num_samples):
        x, y = np.random.uniform(-1, 1, 2)
        distance_squared = x**2 + y**2
        if distance_squared <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4

def visualize_pi_estimation(max_samples: int, step: int = 100) -> None:
    """
    Visualize the convergence of the Monte Carlo π estimation.

    Args:
        max_samples (int): The maximum number of samples to consider for the estimation.
        step (int, optional): The increment of samples for each estimation. Defaults to 100.
    """
    samples = list(range(step, max_samples + 1, step))
    estimates = [estimate_pi(n) for n in samples]

    plt.figure(figsize=(10, 6))
    plt.plot(samples, estimates, label='Monte Carlo Estimate of π', color='blue')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='Actual π Value')
    plt.title('Convergence of Monte Carlo π Estimation')
    plt.xlabel('Number of Samples')
    plt.ylabel('Estimated Value of π')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    visualize_pi_estimation(max_samples=10000)