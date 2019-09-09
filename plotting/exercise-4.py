import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2,1000)

plt.plot(x,np.sqrt(x))
plt.plot(x,x**2)
plt.legend(["cos","sin"],loc='upper left')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.show()