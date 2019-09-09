import matplotlib.pyplot as plt
import numpy as np
def p1(x):return x**4-4*x**2+3*x
def p2(x):return np.sin(10*x)*10
X=np.linspace(-3,3,200)
plt.plot(X,p1(X),X,p2(X))
plt.ylabel('Y-numbers')
plt.xlabel('X-numbers')
plt.show()