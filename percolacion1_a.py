import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



#Punto a

N_semillas=100
probas=np.zeros(N_semillas)
probas_cuad=np.zeros(N_semillas)
l=[4,16,32,64,128]
pc=np.zeros(len(l))
sigma=np.zeros(len(l))
presicion=10**(-3)
cota=-np.log2(presicion)
for k in range(0,len(l)):
	for j in range(0, N_semillas):
		p=0.5
		i=2
		while(i<cota):
			percola= call(["./matriz.e", str(l[k]), str(p) , '1', str(j)])
			if(percola==1):
				p=p-(0.5)**i
			else:
				p=p+(0.5)**i
			i=i+1
		probas[j]=p
		probas_cuad[j]=p**2
	pc[k]=np.mean(probas)
	sigma[k]=np.sqrt(np.mean(probas_cuad)-(pc[k])**2)

plt.figure(1)
plt.scatter(sigma,pc)
plt.show(block=True)

plt.figure(2)
plt.plot(l,0.5927*np.ones(len(l))-pc)
plt.xscale('log')
plt.yscale('log')
plt.show(block=True)





