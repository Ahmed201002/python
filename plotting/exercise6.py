import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,2,.01)
s=np.sin(2*np.pi*t)
plt.plot(t,s)
plt.title(r'$\alpha_i>beta_i$',fontsize=20)
plt.text(1,-.6,r'$\sum_{i=0}^\infty x_i$',fontsize=20)
plt.ylabel('t-time')
plt.xlabel('Volts{mv}')
plt.show()