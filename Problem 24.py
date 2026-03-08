import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 10, 300)
y = np.exp(-x) * np.sin(3*x)

# Create figure
fig, ax = plt.subplots(figsize=(6,4), dpi=120)

# Plot
ax.plot(x, y, linewidth=2)

# Labels and title
ax.set_xlabel('x (dimensionless)', fontsize=12)
ax.set_ylabel(r'$e^{-x}\sin(3x)$', fontsize=12)
ax.set_title('Damped Oscillation: $e^{-x}\sin(3x)$', fontsize=13)

# Tick control
ax.tick_params(axis='both', labelsize=10)

# Clean look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(True, alpha=0.3)

plt.tight_layout()

# Save high resolution
plt.savefig("damped_oscillation.png", dpi=300)

plt.show()