import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,5,300)
I=np.sin(2*t)
E=I**2
fig,ax=plt.subplots(figsize=(8,5))
#Left axis
line1=ax.plot(t,I,color="red",label='I(t)=sin(2t)')
ax.set_xlabel('Time')
ax.set_ylabel('current I(t)',color='red')
#right axis
ax2=ax.twinx()
line2=ax.plot(t,E,color="blue",label='E(t)=I^2')
ax.set_ylabel('Energy E(t)',color='blue')
#combine legends
lines=line1+line2
labels=[l.get_label() for l in lines]
ax.grid(True)
ax.legend(lines, labels)
ax.grid(True)
plt.title('Current and energy Dual axis')
plt.show()
