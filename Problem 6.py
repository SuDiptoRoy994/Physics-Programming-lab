import numpy as np
import matplotlib.pyplot as plt

mass = 1
velocity = np.array([1e7, 2e7, 3e7, 4e7])
c = 3e8

# Classical KE
kinetic_energy = 0.5 * mass * velocity**2

# Relativistic total energy
relativistic_energy = mass * c**2 / np.sqrt(1 - velocity**2 / c**2)

print("Classical KE:")
print(kinetic_energy)

print("Relativistic Energy:")
print(relativistic_energy)

# Plot both vs velocity
plt.plot(velocity, kinetic_energy, label="Classical KE")
plt.plot(velocity, relativistic_energy, label="Relativistic Energy")

plt.xlabel("Velocity")
plt.ylabel("Energy")
plt.title("Energy Comparison")
plt.legend()
plt.show()