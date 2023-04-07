import random

import numpy

# n=65
# x =[]
# for i in range(n):
#     x.append(random.random())

n=5
x =[0,0.25,0.5,0.75,1]
import numpy as np
x=np.sort(x)
dx=[]
for i in range(n-1):
    i=i+1
    dx.append(x[i]-x[i-1])
S=np.zeros((n-2,n-2))
for i in range(n-2):
    S[i,i]=(1/dx[i])+(1/dx[i+1])
for i in range(n-3):
    S[i,i+1]=(-1/dx[i+1])
for i in range(n-3):
    S[i+1,i]=(-1/dx[i+1])
SS=[]
SS=np.zeros(n-2)
for i in range(n-2):
    SS[i]=(dx[i]+dx[i+1])/2
U=np.linalg.solve(S,SS)
import numpy
U_t=numpy.append(U,[0])
U_t=numpy.append([0],U_t)

import matplotlib.pyplot as plt
plt.plot(x,U_t)


U_x=[]
xx=np.linspace(0,1,num=500)
for i in range(len(xx)):
    U_x.append(-xx[i]**2/2+xx[i]/2)
plt.plot(xx,U_x)
plt.show()
