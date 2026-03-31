import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 2000)

fig, ax = plt.subplots(figsize=(6,4))

# Histogram
ax.hist(data, bins=40, density=True, alpha=0.6)

# Mean line
mean = np.mean(data)
ax.axvline(mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')

ax.set_xlabel('Value')
ax.set_ylabel('Probability Density')
ax.set_title('Normal Distribution Histogram')
ax.legend()

ax.grid(True, alpha=0.3)

plt.show()