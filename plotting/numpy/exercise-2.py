import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.005)
y=np.exp(-x/2.)*np.sin(2*np.pi*x)
plt.plot(x,y)
plt.xlim(0,10)
plt.ylim(-1,1)
plt.show()

