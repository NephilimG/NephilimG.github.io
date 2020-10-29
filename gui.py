import tkinter
import numpy as np
import matplotlib.pyplot as plt
 
top = tkinter.Tk()
 
def CAllBack():
   plt.subplot(323)
   y3=[1,0,0,0,0,0,0,0,0]
   plt.stem(y3)
   plt.grid(True)
   plt.show()
def CBllBack():
  x=np.linspace(0,5,20)
  x1=np.linspace(0,10,10)
  X=[2,1.5,1,0.5]
  y1=[]
  for i in range(32):
    y1.append(X[i%4])
  plt.subplot(321)
  plt.stem(list(y1))
  plt.grid(True)
  plt.show()
def CCllBack():
  plt.subplot(324)
  y4=[0,0,0,1,1,1,1]
  plt.stem(y4)
  plt.grid(True)
  plt.show()
def CDllBack():
  x=np.linspace(0,5,20)
  x1=np.linspace(0,10,10)
  X=[2,1.5,1,0.5]
  y1=[]
  for i in range(32):
    y1.append(X[i%4])
  plt.subplot(325)
  A=2
  a=0.6
  y5=A*a**x1
  plt.grid(True)
  plt.stem(x1,y5)
  plt.show()
B = tkinter.Button(top, text ="冲激", command = CAllBack)
A = tkinter.Button(top, text ="周期", command = CBllBack)
C = tkinter.Button(top, text ="阶跃", command = CCllBack)
D = tkinter.Button(top, text ="实指数", command = CDllBack)
 
B.pack()
A.pack()
C.pack()
D.pack()
top.mainloop()