import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as spline
from subprocess import call




datos=np.loadtxt('dim_fractal',dtype=float)








l=datos[:,0]
m=datos[:,5]

P=np.zeros(len(m))

for i in range(1,len(l)):
	P[i]=m[i]/(l[i]*l[i])		

p=np.polyfit(np.log(l[2:30]),np.log(m[2:30]),1)

plt.figure(1)
plt.scatter(np.log(l[2:101]),np.log(m[2:101]),s=2)
plt.plot(np.log(l[2:101]),np.polyval(p,np.log(l[2:101])))
plt.show(block=True)

D=91/48


rango=30

lab=''

for i in range(2,6):
    D=np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,i]),1)[0]
    lab =lab + 'D = {}'.format(D)

size=2

plt.figure(1)
line1 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,2]),s=size,label=lab[0:22])
line1a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,2]),1),np.log(l[2:101])))

line2 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,3]),s=size,label=lab[22:44])
line2a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,3]),1),np.log(l[2:101])))

line3 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,4]),s=size,label=lab[44:66])
line3a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,4]),1),np.log(l[2:101])))

line4 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,5]),s=size,label=lab[66:88])
line4a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,5]),1),np.log(l[2:101])))

plt.xlabel('Log(L)')
plt.ylabel('Log(M)')
#axes = plt.gca()
#axes.set_xlim([0.55,0.63])
#axes.set_ylim([0.55,0.65])
legend1 = plt.legend(handles=[line1,line2,line3,line4], loc='Best')
plt.show(block=True)




