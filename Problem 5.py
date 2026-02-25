import numpy as np
import matplotlib.pyplot as plt
# Data
k=500
Displacement=np.array([0.01,0.02,0.03,0.04,0.05,0.06])
#Compute Spring potential energy
spring_potential_energy=0.5*k*Displacement**2
#Plot Potential energy vs Displacement
plt.plot(Displacement, spring_potential_energy)
plt.xlabel('Displacement')
plt.ylabel('Spring Potential Energy')
plt.title('Spring Potential Energy vs Displacement')
plt.grid(True)
plt.show()

