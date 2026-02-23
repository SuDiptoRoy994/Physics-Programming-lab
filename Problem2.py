import numpy as np
import matplotlib.pyplot as plt
#Data
mass=[2]
velocity=np.linspace(0,12)
#loop over mass
for mass in mass:
    kinetic_energy=0.5*mass*velocity**2

#Plot kinetic energy vs velocity graph
plt.plot(velocity,kinetic_energy)
plt.xlabel('velocity')
plt.ylabel('kinetic energy')
plt.title('kinetic energy vs velocity')
plt.grid(True)
plt.show()


