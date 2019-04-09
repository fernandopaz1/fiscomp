import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



#Punto a

datos=np.loadtxt('pc',dtype=float)


iteraciones=27000


dim=[4,8,16,32,64]
p_l=np.zeros(len(dim))
p_cuad_l=np.zeros(len(dim))
masa=np.zeros(len(dim))
sigma=np.zeros(len(dim))

for i in range(0,len(dim)):
	for k in range(0,iteraciones):
		p_l[i]=p_l[i]+datos[k+i*iteraciones,1]
		p_cuad_l[i]=p_cuad_l[i]+datos[k+i*iteraciones,2]
		masa[i]=masa[i]+datos[k+i*iteraciones,4]
	
		
p_l=p_l/iteraciones
p_cuad_l=p_cuad_l/iteraciones
masa=masa/iteraciones

for i in range(0,len(dim)):
	sigma[i]= np.sqrt(p_cuad_l[i] - (p_l[i])*(p_l[i]))
	

plt.figure(1)
plt.scatter(dim,p_l)
plt.xscale('log')
plt.yscale('log')
plt.show(block=True)


plt.figure(2)
plt.scatter(sigma,p_l)
plt.xscale('log')
plt.yscale('log')
plt.show(block=True)
