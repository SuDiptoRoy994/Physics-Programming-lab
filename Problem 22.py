import numpy as np
import matplotlib.pyplot as plt

# Data
masses = [1, 2, 4]
velocity = np.linspace(0, 15, 200)

# Create figure
fig, ax = plt.subplots(figsize=(8,5))

# Loop over masses
for m in masses:
    kinetic_energy = 0.5 * m * velocity**2
    ax.plot(velocity, kinetic_energy, label=f'm = {m}')

# Formatting
ax.set_xlabel('Velocity')
ax.set_ylabel('Kinetic Energy')
ax.set_title('Kinetic Energy vs Velocity for Different Masses')
ax.legend()
ax.grid(True)

plt.show()