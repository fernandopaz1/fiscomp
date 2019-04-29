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

rango_min=4
rango=80
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
y=np.log(datos[2,rango_min:rango])
p=np.polyfit(x,y,1)
line1 = plt.scatter(x,y,s=size,label='ns')
line2, = plt.plot(x,np.polyval(p,x),label='Ajuste lineal')
plt.xlabel('log(s)')
plt.ylabel('log(ns)')
legend1 = plt.legend(handles=[line1,line2], loc='Best')
plt.show()

plt.figure(2)
line1 = plt.scatter(datos[:,0],chi_squared,s=size,label='$\\chi$')
legend1 = plt.legend(handles=[line1], loc='Best')
plt.xlabel('p')
plt.ylabel('Error cuadratico')
plt.show()





np.min(chi_squared)
indice_optimo=np.where(chi_squared == min(chi_squared))[0][0]
pc_64=datos[indice_optimo,0]
tau=taus[indice_optimo]


print('El valor de taus es:  ',tau)

pc64=0.59256
#pc64=datos[indice_optimo,0]


pmax=np.zeros(len(datos[0,:])-1)

natural=np.zeros(len(pmax))
for i in range(1,len(pmax)):
    a=max(datos[1:len(datos[:,0]),i])
    ind_max=int(np.where(datos[:,i] == a)[0][0])
    pmax[i]=datos[ind_max,0]
    natural[i]=i+1;



argum=(pmax-pc64*np.ones(len(pmax)))
fin=len(argum)
x=(natural[1450:1700])
y=(argum[1450:1700])
plt.figure(4)
plt.scatter(x,y,s=size)
p2=np.polyfit(x,y,1)
plt.plot(x,p2[0]*x+p2[1]*np.ones(len(x)))
#plt.xscale('log')
#plt.yscale('log')
plt.show()



a=np.ones(len(datos[:,0]))

b=0.242
plt.figure(5)
line3 = plt.scatter((datos[:,0]-pc64*a)*(3**b),datos[:,3]/datos[12,3],s=size,label='s=3')
line2 = plt.scatter((datos[:,0]-pc64*a)*(2**b),datos[:,2]/datos[12,2],s=size,label='s=2')
line4 = plt.scatter((datos[:,0]-pc64*a)*(4**b),datos[:,4]/datos[12,4],s=size,label='s=4')
line5 = plt.scatter((datos[:,0]-pc64*a)*(5**b),datos[:,5]/datos[12,5],s=size,label='s=5')
line6 = plt.scatter((datos[:,0]-pc64*a)*(6**b),datos[:,6]/datos[12,6],s=size,label='s=6')
line7 = plt.scatter((datos[:,0]-pc64*a)*(50**b),datos[:,50]/datos[12,50],s=size,label='s=50')
plt.xlabel('z')
plt.ylabel('$\\frac{<ns(p)>}{<ns(p_c)>}$')
legend1 = plt.legend(handles=[line2,line3,line4,line5,line6,line7], loc='Best')
plt.show()


print('El coeficiente $\\sigma$ es: ',b)

