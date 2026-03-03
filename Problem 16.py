import numpy as np
import matplotlib.pyplot as plt
# create Data
t=np.linspace(0,1,500)
y=np.exp(-0.2*t)*np.cos(2*np.pi*t)
#create figure and axis
fig,ax=plt.subplots(figsize=(8,5))
#Plot
ax.plot(t,y,label='Damped Oscillation')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Damped Oscillation')
ax.legend()
ax.grid(True)
plt.show()