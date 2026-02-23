import numpy as np
import matplotlib.pyplot as plt
#define mass and velocity
mass=np.array([1.0,1.5,2.0,2.5,3.0])
velocity=np.array([2,4,6,8,10])
# compute momentum
momentum=mass*velocity
print(momentum)
#plot momentum vs velocity
plt.plot(momentum,velocity)
plt.xlabel('velocity')
plt.ylabel('momentum')
plt.title('momentum vs velocity')
plt.show()