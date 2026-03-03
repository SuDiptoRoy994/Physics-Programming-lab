import numpy as np
import matplotlib.pyplot as plt
#Data
x=np.linspace(0,1,100)
# Create 2x2 layout
fig,ax=plt.subplots(2,2,figsize=(8,6))
#Plot 1:y=x
ax[0,0].plot(x,x,color='blue')
ax[0,0].set_title("y=x")
ax[0,0].grid(True)
#Plot 2:y=x^2
ax[0,1].plot(x,x**2,color='red')
ax[0,1].set_title("y=x^2")
ax[0,1].grid(True)
#Plot 3:y=x^3
ax[1,0].plot(x,x**3,color='green')
ax[1,0].set_title("y=x^3")
ax[1,0].grid(True)
#Plot 4:y=sqrt(x)
ax[1,1].plot(x,np.sqrt(x),color='purple')
ax[1,1].set_title("y=sqrt(x)")
ax[1,1].grid(True)
fig.tight_layout()
plt.show()