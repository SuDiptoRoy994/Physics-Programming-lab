import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 400)
y = np.exp(-0.3*t) * np.cos(4*t)

fig, ax = plt.subplots(figsize=(6,4))

ax.plot(t, y, label='Damped Oscillation')

# Fill only positive region
ax.fill_between(t, y, where=(y >= 0), alpha=0.3)

ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Damped Oscillation')
ax.legend()

ax.grid(True, alpha=0.3)

plt.show()