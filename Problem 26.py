import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(-5, 5, 200)
y1 = x**2
y2 = x**3

# Figure
fig, ax = plt.subplots(figsize=(6,4), dpi=120)

# Plot
ax.plot(x, y1, linestyle='-', label=r'$y = x^2$')
ax.plot(x, y2, linestyle='--', label=r'$y = x^3$')

# Labels
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Comparison of $x^2$ and $x^3$', fontsize=13)

# Styling
ax.legend()
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("comparison_plot.png", dpi=300)

plt.show()