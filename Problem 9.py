import numpy as np
import matplotlib.pyplot as plt

t = np.array([1,2,3,4,5,6])

# Position
x = 5 * t

plt.subplot(2,1,1)
plt.plot(t, x,color='red')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Position vs Time')
plt.grid()

# Velocity (constant)
velocity = np.full_like(t, 5)

plt.subplot(2,1,2)
plt.plot(t, velocity)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity vs Time')
plt.grid()

plt.tight_layout()
plt.show()