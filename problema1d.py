import numpy as np
import math as mt
import matplotlib.pyplot as plt
import scipy.special as sp
from scipy.optimize import leastsq


datos=np.loadtxt('distribucion_fragmentos64', delimiter=" ")


probas=len(datos[:,0])
chi_squared=np.zeros(probas)
taus=np.zeros(probas)

nat=np.zeros(len(datos[1,:]))

#rango=len(datos[1,:])

rango_min=200
rango=500


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
