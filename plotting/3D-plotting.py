import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
x,y=np.meshgrid(x,y)
R=np.sqrt(x**2+y**2)
z=np.sin(R)
ax.plot_surface(x,y,z,cmap='hot')
plt.show()