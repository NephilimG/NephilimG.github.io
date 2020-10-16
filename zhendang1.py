import numpy as np
import matplotlib.pyplot as plt
import numpy as A
import numpy as w 
import numpy as a 
import numpy as c
a=2.718281828459
c=1
w=50
x=np.arange(-1,1,0.01)
A=pow(a,c*x)
y=A*np.cos(w*x)

plt.plot(x,y)
plt.show()