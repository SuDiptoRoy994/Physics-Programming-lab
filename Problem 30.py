import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 300)
I = np.sin(2*t)
E = I**2

fig, ax = plt.subplots(figsize=(6,4))

# Left axis
line1 = ax.plot(t, I, label='I(t)', color='blue')
ax.set_xlabel('Time')
ax.set_ylabel('Current', color='blue')

# Right axis
ax2 = ax.twinx()
line2 = ax2.plot(t, E, label='E(t)', color='red')
ax2.set_ylabel('Energy', color='red')

# Combine legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax.legend(lines, labels)

ax.grid(True, alpha=0.3)

plt.title('Current and Energy')

plt.show()