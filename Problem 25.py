import numpy as np
import matplotlib.pyplot as plt

# Data
m = 2
v = np.linspace(0, 12, 200)
KE = 0.5 * m * v**2

# Figure
fig, ax = plt.subplots(figsize=(6,4), dpi=120)

# Plot
ax.plot(v, KE, linewidth=2)

# Labels and title
ax.set_xlabel('Velocity (m/s)', fontsize=12)
ax.set_ylabel('Kinetic Energy (J)', fontsize=12)
ax.set_title('Kinetic Energy vs Velocity', fontsize=13)

# Styling
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', labelsize=10)

plt.tight_layout()
plt.savefig("kinetic_energy_plot.png", dpi=300)

plt.show()
