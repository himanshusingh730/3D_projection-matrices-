from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import math
a=[]
b=[]
#Defining the 3D funtion
x = np.arange(0,50,0.1)
for i in np.arange(0,50,0.1):
	a.append(math.sin (i))
y = np.array(a)
for j in np.arange(0,50,0.1):
	b.append(math.cos(j))
z = np.array(b)
#arrays to the matrix
poin= np.matrix(np.vstack([x,y,z]))
#defining angles and the plane of projection
ajj=20#degree
amm=90#degree
jj=ajj*(math.pi/180)
mm=amm*(math.pi/180)
a1=math.sin(jj)
a2=0
a3=math.cos(jj)
b1=-math.sin(mm)*math.cos(jj)
b2=math.cos(mm)
b3=math.sin(mm)*math.sin(jj)
#project the 3D funtion on the plane
zoin= np.matrix([[a1,a2,a3],[b1,b2,b3]])
tot=np.matmul(zoin,poin)
#devide the output matrix into two matrices
axison=[1,0]
axistw=[0,1]
alpha=np.matmul(axison,tot)
glo=np.array(alpha)
beta = np.matmul(axistw,tot)
glp=np.array(beta)
#convert output matrices into the arrays
one=np.squeeze(glo)
two=np.squeeze(glp)
plt.plot(one,two)
plt.show()
