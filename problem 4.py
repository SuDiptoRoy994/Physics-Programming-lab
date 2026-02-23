import numpy as np
import matplotlib.pyplot as plt
mass = 2
Heights = np.array([1,2,3,4,5,6])
g = 9.81

potential_energy = mass * g * Heights

plt.plot(Heights, potential_energy)
plt.xlabel('Height')
plt.ylabel('Potential Energy')
plt.title('Potential Energy vs Height')
plt.show()