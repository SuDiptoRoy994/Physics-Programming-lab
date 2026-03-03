import numpy as np
import matplotlib.pyplot as plt
# Data
t=np.linspace(0,10,200)
y1=np.sin(t)
y2=np.exp(-0.3*t)
# figure and main axis
fig,ax=plt.subplots(figsize=(10,5))
#Left axis Plot
line1=ax.plot(t,y1,color='r',label='sin(t)')
ax.set_xlabel('time')
ax.set_ylabel('sin(t)',color='r')
#Right axis Plot
line2=ax.plot(t,y2,color='b',label='exp(-0.3t)')
ax.set_xlabel('time')
ax.set_ylabel('exp(-0.3t)',color='b')
#combine legends
lines=line1+line2
labels=[l.get_label() for l in lines]
ax.legend(lines, labels)
ax.grid(True)
plt.title('Sine and Exponential on Dual Axes')
plt.show()
