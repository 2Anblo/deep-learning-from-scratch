import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)
    
x = np.arange(-10.0, 10.0, 1)
y = relu(x)

plt.plot(x, y)
plt.ylim(-1.1, 10.1) # 指定y轴范围
plt.show()