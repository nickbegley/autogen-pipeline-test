"""
Module for estimating the value of π using the Monte Carlo method.

This module provides a function to estimate π and visualize the convergence
of the estimation with a scatter plot. It requires the `matplotlib` and
`numpy` libraries for visualization and numerical operations.
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_samples: int) -> float:
    """
    Estimate the value of π using the Monte Carlo method.
    
    Args:
        num_samples (int): The number of random samples to generate for estimation.
        
    Returns:
        float: The estimated value of π.

    Raises:
        ValueError: If num_samples is not a positive integer.
    """
    if num_samples <= 0:
        raise ValueError("num_samples must be a positive integer")
    
    inside_circle = 0

    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    return (inside_circle / num_samples) * 4

def visualize_pi_convergence(max_samples: int, step: int) -> None:
    """
    Visualize the convergence of the Monte Carlo π estimation.
    
    Args:
        max_samples (int): The maximum number of samples to use for estimation.
        step (int): The step size for increasing the number of samples.
    """
    samples = list(range(step, max_samples + 1, step))
    estimates = [estimate_pi(n) for n in samples]

    plt.figure(figsize=(10, 6))
    plt.plot(samples, estimates, label='Estimate of π', marker='o')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='Actual π')
    plt.title('Monte Carlo Estimation of π')
    plt.xlabel('Number of Samples')
    plt.ylabel('Estimated Value of π')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    visualize_pi_convergence(max_samples=10000, step=100)