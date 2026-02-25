import numpy as np
import matplotlib.pyplot as plt
N0=1000
time=np.array([1,2,3,4,5])
lam=0.5
N=N0*np.exp(-lam*time)
print(N)
plt.plot(time,N)
plt.xlabel('time')
plt.ylabel('Quantity N(t)')
plt.title('Radioactive Decay')
plt.grid(True)
plt.show()
