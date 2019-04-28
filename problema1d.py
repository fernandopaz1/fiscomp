import numpy as np
import math as mt
import matplotlib.pyplot as plt
import scipy.special as sp
from scipy.optimize import leastsq


datos=np.loadtxt('distribucion_fragmentos', delimiter=" ")


probas=len(datos[:,0])
chi_squared=np.zeros(probas)
taus=np.zeros(probas)

nat=np.zeros(len(datos[1,:]))

rango_min=100
rango=700
#rango=len(datos[1,:])


size=2


x=np.log(range(rango_min,rango))
for i in range(0,probas):
    y=np.log(datos[i,rango_min:rango])
    p=np.polyfit(x,y,1)
    taus[i]=p[0]
    chi_squared[i]=np.sum((np.polyval(p,x)-y)**2)
    
 
plt.figure(1)
x=np.log(range(rango_min,rango))
y=np.log(datos[100,rango_min:rango])
p=np.polyfit(x,y,1)
line1 = plt.scatter(x,y,s=size)
line2 = plt.plot(x,np.polyval(p,x))
plt.show()

plt.figure(2)
plt.scatter(datos[:,0],chi_squared,s=size)
plt.show()



plt.figure(3)
plt.scatter(datos[:,0],taus,s=size)
plt.show()

np.min(chi_squared)
indice_optimo=np.where(chi_squared == min(chi_squared))[0][0]
pc_64=datos[indice_optimo,0]
taus[indice_optimo]

#pc64=0.59256
pc64=datos[indice_optimo,0]


pmax=np.zeros(len(datos[0,:])-1)

natural=np.zeros(len(pmax))
for i in range(1,len(pmax)):
    a=max(datos[1:len(datos[:,0]),i])
    ind_max=int(np.where(datos[:,i] == a)[0][0])
    pmax[i]=datos[ind_max,0]
    natural[i]=i+1;



argum=pc64*np.ones(len(pmax))-pmax
fin=len(argum)
plt.figure(3)
plt.scatter(natural[3:fin],argum[3:fin],s=size)
#plt.xscale('log')
#plt.yscale('log')
plt.show()


plt.figure(4)
line1 = plt.scatter(datos[:,0],datos[:,1],s=size,label='1')
line2 = plt.scatter(datos[:,0],datos[:,2],s=size,label='2')
##plt.scatter(datos[:,0],datos[:,100],s=size)
plt.xscale('log')
plt.yscale('log')
legend1 = plt.legend(handles=[line1,line2], loc='Best')
plt.show()

