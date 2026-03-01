import numpy as np
import matplotlib.pyplot as plt
mass1=1
mass2=2
velocity=np.linspace(0,10,100)
ke1=0.5*mass1*velocity**2
ke2=0.5*mass2*velocity**2
plt.plot(velocity,ke1,linestyle='--',label='Mass=1',color='r')
plt.plot(velocity,ke2,linestyle='-',label='Mass=2',color='b')
plt.xlabel('Velocity')
plt.ylabel('Kinetic Energy')
plt.legend()
plt.grid(True)
plt.show()