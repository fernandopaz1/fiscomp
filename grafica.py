import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



#Punto a

pc_l_semilla=np.loadtxt('pc_l_semilla.txt',dtype=float)
l=np.loadtxt('largo_red',dtype=long)

pc_l=np.zeros(len(l))
p_cuad=np.zeros((len(l),len(pc_l_semilla[0,:])))
p_cuad_med=np.zeros(len(l))
sigma_l=np.zeros(len(l))



for k in range(0,len(l)):
	for i in range(0,len(pc_l_semilla[0,:])):
		p_cuad[k,i]=pc_l_semilla[k,i]**2
	pc_l[k]=np.mean(pc_l_semilla[k,:])
	p_cuad_med[k]=np.mean(p_cuad[k,:])
	sigma_l[k]=np.sqrt(p_cuad_med[k]-pc_l[k]**2)

plt.figure(1)
plt.scatter(sigma_l,pc_l)
plt.show(block=True)


#plt.figure(2)
#plt.plot(l,0.5927*np.ones(len(l))-pc)
#plt.xscale('log')
#plt.yscale('log')
#plt.show(block=True)


