import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm, assoc_laguerre
import math

# Constants
pi = np.pi

# Function to compute radial part of wavefunction (R_nl)
def radial_wavefunction(n, l, r):
    rho = 2 * r / n
    norm = np.sqrt((2 / n) ** 3 * math.factorial(n - l - 1) / (2 * n * math.factorial(n + l)))
    laguerre = assoc_laguerre(rho, n - l - 1, 2 * l + 1)
    radial = norm * np.exp(-rho / 2) * rho ** l * laguerre
    return radial

# Function to compute angular part of wavefunction (Y_lm)
def angular_wavefunction(l, m, theta, phi):
    return sph_harm(m, l, phi, theta)

# Full wavefunction R_nl * Y_lm
def wavefunction(n, l, m, r, theta, phi):
    R = radial_wavefunction(n, l, r)
    Y = angular_wavefunction(l, m, theta, phi)
    psi = R * Y
    return np.abs(psi) ** 2  # Probability distribution

# Generate a spherical grid
def generate_grid(size_r=50, size_theta=50, size_phi=50):
    r = np.linspace(0, 20, size_r)
    theta = np.linspace(0, pi, size_theta)
    phi = np.linspace(0, 2 * pi, size_phi)
    r, theta, phi = np.meshgrid(r, theta, phi)
    return r, theta, phi

# Convert spherical coordinates to cartesian for plotting
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# Plot the probability distribution with a scatter plot for 3D visualization
def plot_wavefunction(n, l, m):
    r, theta, phi = generate_grid(size_r=30, size_theta=30, size_phi=30)  # Reduced grid size for speed
    psi_squared = wavefunction(n, l, m, r, theta, phi)
    
    x, y, z = spherical_to_cartesian(r, theta, phi)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(f'Quantum Numbers n={n}, l={l}, m={m}')

    # Use scatter plot to visualize the 3D probability distribution
    ax.scatter(x, y, z, c=psi_squared.ravel(), cmap='viridis', marker='o', alpha=0.5)

    # Improve performance by removing axes for a cleaner look
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    fig.colorbar(ax.scatter(x, y, z, c=psi_squared.ravel(), cmap='viridis', marker='o', alpha=0.5), ax=ax, shrink=0.5, aspect=5)  # Add color bar to indicate intensity
    plt.show()

# Input quantum numbers n, l, m
def main():
    print("Quantum Number Pattern Visualizer")
    n = int(input("Enter principal quantum number n (1, 2, 3, ...): "))
    l = int(input(f"Enter angular momentum quantum number l (0, 1, 2, ..., n-1): "))
    m = int(input(f"Enter magnetic quantum number m (-l, ..., 0, ..., +l): "))
    
    plot_wavefunction(n, l, m)

if __name__ == "__main__":
    main()
