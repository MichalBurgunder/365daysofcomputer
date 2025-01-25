import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import maxwell

# Set parameters for the Maxwell-Boltzmann distribution
temperature = 292  # in Kelvin
k_b = 1.38e-23  # Boltzmann constant in J/K
mass_hydrogen = 1.66e-27  # mass of a hydrogen atom in kg

# Calculate the scale parameter for the Maxwell distribution (sqrt(kT/m))
scale_param = np.sqrt(k_b * temperature / mass_hydrogen)

# Generate a range of speeds and corresponding probability densities
speeds = np.linspace(0, 8000, 8000)  # range of speeds in m/s
probability_densities = maxwell.pdf(speeds, scale=scale_param)

num_bins = 70
plt.figure(figsize=(10, 6))
plt.hist(speeds, bins=num_bins, weights=probability_densities, color=(62/256, 19/256, 139/256), edgecolor='black')
plt.title("Maxwell-Boltzmann Distribution at 292K")
plt.xlabel("Speed (m/s)")
plt.ylabel("Probability Density")
plt.show()

# Plot the Maxwell-Boltzmann distribution
# plt.figure(figsize=(10, 6))
# plt.plot(speeds, probability_densities, color='blue', lw=2)
# plt.title("Maxwell-Boltzmann")
# plt.xlabel("Speed (m/s)")
# plt.ylabel("Probability Density")
# plt.grid(True)
# plt.show()

