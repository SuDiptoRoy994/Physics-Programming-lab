import numpy as np
import matplotlib.pyplot as plt
#Data
x=np.linspace(0,2*np.pi,400)
y=np.sin(x)
#create figure
fig, ax = plt.subplots(figsize=(8,6))
#Plot sine curve
ax.plot(x,y,color='blue',label="y=sin(x)")
#fill area under the curve
ax.fill_between(x,y,alpha=0.3)
#label and formatting
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Sine curved with filled area')
ax.legend()
ax.grid()
plt.show()