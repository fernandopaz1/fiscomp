import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



#Punto a

N_semillas=1000
l=[4,16,32,64,128]
probas=np.zeros((len(l),N_semillas))
presicion=10**(-3)
cota=-np.log2(presicion)

ind_ant=0

probas_anteriores=np.loadtxt('pc_l_semilla.txt',dtype=float)
ind_ant=np.load('iteracion_semilla.npy')
a=ind_ant+N_semillas

for k in range(0,len(l)):
	for j in range(ind_ant, ind_ant+N_semillas):
		p=0.5
		i=2
		while(i<cota):
			percola= call(["./matriz.e", str(l[k]), str(p) , '1', str(j)])
			if(percola==1):
				p=p-(0.5)**i
			else:
				p=p+(0.5)**i
			i=i+1
		probas[k,j-ind_ant]=p
	
		
probas=np.concatenate((probas, probas_anteriores), axis=1)


np.savetxt('largo_red',l)                  
np.savetxt('pc_l_semilla.txt',probas)
np.save('iteracion_semilla',a)
