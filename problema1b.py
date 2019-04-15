import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as spline
from subprocess import call




datos=np.loadtxt('distribucion_perco',dtype=float)



iteraciones=27000
a=len(datos[:,1])/iteraciones

dim=64


p=np.linspace(0.01,0.99,a)
paso=p[1]-p[0]
cuento_precolaciones=np.zeros(len(p))


for i in range(0,len(p)):
	for k in range(0,iteraciones):
		cuento_precolaciones[i]=cuento_precolaciones[i]+datos[k+i*iteraciones,1]
	
	
cuento_precolaciones=cuento_precolaciones/iteraciones


#print(cuento_precolaciones[59])

#exit()
indice=0
for i in range(0,len(p)) :
	if(cuento_precolaciones[i]>0.5):		#Este indice es el del primer elemento mayor a 0.5
		indice=i
		print(cuento_precolaciones[i])
		break		



print("El indice es:   ", indice)

i=indice
a=(cuento_precolaciones[i]-cuento_precolaciones[i-1])/(p[i]-p[i-1])
b=cuento_precolaciones[i-1]					#La interpolacion es a*x+b

print("El punto mas cercanos es:   ", b)

def interpol(x,a,b):
	f=a*(x-p[i-1])+b
	return f							#La inversa si evaluo en 0.5 me deberia dar pc


def invers(x,a,b):
	inver=(x-b)/a+p[i-1]
	return inver							#La inversa si evaluo en 0.5 me deberia dar pc



pc=invers(0.5,a,b)
x=np.linspace(-0.03+pc,0.03+pc,100)
y=np.zeros(len(x))
for j in range(0,len(x)):
	y[j]=interpol(x[j],a,b)

linea1=[0,pc]             #Horizontal
linea2=[0,0.5]		#vertical

print("La porbabilidad critica es:   ", pc)

plt.figure(1)
plt.scatter(p,cuento_precolaciones)
plt.plot(x,y)
plt.plot(linea1,0.5*np.ones(len(linea1)))
plt.plot(pc*np.ones(len(linea2)),linea2)
plt.show(block=True)


