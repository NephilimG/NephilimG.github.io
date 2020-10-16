import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(-3, 10, 0.1)
 
y = 2*np.cos(x+2)
plt.plot(x, y)
 
plt.show()
