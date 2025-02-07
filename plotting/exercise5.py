import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(0,5,0.1)
t2=np.arange(0,5,.02)
plt.figure()
plt.subplot(311)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(312)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.subplot(313)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')


plt.show()