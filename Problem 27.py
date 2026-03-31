import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 10, 200)
x_log = np.linspace(0.1, 10, 200)  # for ln(x)

# Figure
fig, axs = plt.subplots(2, 2, figsize=(8,6))

# Plot 1: y = x
axs[0,0].plot(x, x)
axs[0,0].set_title('y = x')
axs[0,0].grid(True)

# Plot 2: y = x^2
axs[0,1].plot(x, x**2)
axs[0,1].set_title('y = x^2')
axs[0,1].grid(True)

# Plot 3: y = e^x
axs[1,0].plot(x, np.exp(x))
axs[1,0].set_title('y = e^x')
axs[1,0].grid(True)

# Plot 4: y = ln(x)
axs[1,1].plot(x_log, np.log(x_log))
axs[1,1].set_title('y = ln(x)')
axs[1,1].grid(True)

fig.tight_layout()
plt.show()