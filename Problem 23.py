import numpy as np
import matplotlib.pyplot as plt

v = np.linspace(0, 10, 300)
m = 2
KE = 0.5 * m * v**2

fig, ax = plt.subplots(figsize=(6,4), dpi=120)

ax.plot(v, KE, linewidth=2)

ax.set_xlabel('Velocity (m/s)', fontsize=12)
ax.set_ylabel('Kinetic Energy (J)', fontsize=12)
ax.set_title('Kinetic Energy vs Velocity', fontsize=13)

ax.tick_params(axis='both', labelsize=10)

# Remove top and right spines (clean look)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig("ke_plot.png", dpi=300)
plt.show()