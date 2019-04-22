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

#rango=len(datos[1,:])
rango=1500


ns=lambda tpl,x : -tpl[0]*x-np.log(sp.zeta(tpl[0]-1))+np.log(tpl[1])

def ErrorFunc(tpl,x,y):
    if(tpl[0]>2.04 and tpl[0]<3):
        return ns(tpl,x)-y
    else:
        return 1e10*np.ones(len(x))




x=np.log(range(2,rango))
for i in range(0,probas):
    y=np.log(datos[i,2:rango])
    p=np.polyfit(x,y,1)
    #b=sp.zeta(2.05-1)*np.exp(p[1])
    tplInitial1=(2.041, 100)
    tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x,y),maxfev=1000)
    taus[i]=tplFinal1[0]
    chi_squared[i]=np.sum(ErrorFunc(tplFinal1,x,y)**2)
    
 
plt.figure(1)
x=np.log(range(2,rango))
y=np.log(datos[1270,2:rango])
p=np.polyfit(x,y,1)
tplInitial1=(2.04,10)
tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x,y),maxfev=1000)
line1 = plt.scatter(x,y,s=1)
line2 = plt.plot(x,ns(tplFinal1,x))
line2 = plt.plot(x,np.polyval(p,x))
#plt.xscale("log")
#plt.yscale("log")
plt.show()

plt.figure(2)
plt.scatter(datos[:,0],chi_squared)
plt.show()


plt.figure(3)
plt.scatter(datos[:,0],taus)
plt.show()
