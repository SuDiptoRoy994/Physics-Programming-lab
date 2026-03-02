import numpy as np
import matplotlib.pyplot as plt
mass1=1
mass2=3
mass3=5
velocity=np.linspace(0,20,200)
ke1=0.5*mass1*velocity**2
ke2=0.5*mass2*velocity**2
ke3=0.5*mass3*velocity**2
plt.plot(velocity, ke1,ls="-",label="mass=1")
plt.plot(velocity, ke2,ls="--",label="mass=3")
plt.plot(velocity, ke3,ls=":",label="mass=5")
plt.xlabel("Velocity")
plt.ylabel("Kinetic Energy")
plt.title("Kinetic Energy vs Velocity")
plt.legend()
plt.grid()
plt.show()