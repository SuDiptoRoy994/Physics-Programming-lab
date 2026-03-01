import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
N0 = 1000
lam = 0.5

# Time array (smooth curve)
t = np.linspace(0, 10, 100)

# Compute decay
N = N0 * np.exp(-lam * t)

# Create figure with two subplots (top and bottom)
plt.figure(figsize=(6,8))

# -------------------
# Normal Plot
# -------------------
plt.subplot(2,1,1)
plt.plot(t, N)
plt.title("Exponential Decay (Normal Scale)")
plt.xlabel("Time")
plt.ylabel("N(t)")
plt.grid()

# -------------------
# Log Plot
# -------------------
plt.subplot(2,1,2)
plt.plot(t, N)
plt.yscale("log")
plt.title("Exponential Decay (Log Scale)")
plt.xlabel("Time")
plt.ylabel("log N(t)")
plt.grid()

plt.tight_layout()
plt.show()