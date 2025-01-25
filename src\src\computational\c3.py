"""
Module for estimating π using the Monte Carlo method and visualizing the convergence.

This module contains functions to perform the Monte Carlo estimation of π and
to visualize the process of convergence as more points are sampled.
"""

import matplotlib.pyplot as plt
import numpy as np

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.

    Parameters:
        num_samples (int): The number of random samples to generate.

    Returns:
        float: The estimated value of π.
    """
    inside_circle = 0

    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4

def visualize_pi_estimation(num_samples: int) -> None:
    """
    Visualize the convergence of the Monte Carlo estimation of π.

    Parameters:
        num_samples (int): The number of random samples to generate for the estimation.
    """
    estimates = []
    inside_circle_counts = 0

    for i in range(1, num_samples + 1):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle_counts += 1
        estimate = (inside_circle_counts / i) * 4
        estimates.append(estimate)

    plt.figure(figsize=(10, 5))
    plt.plot(estimates, label='Estimate of π', color='blue')
    plt.axhline(y=np.pi, color='red', linestyle='--', label='Actual π')
    plt.title('Monte Carlo Estimation of π')
    plt.xlabel('Number of Samples')
    plt.ylabel('Estimated Value of π')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Example usage
    visualize_pi_estimation(10000)