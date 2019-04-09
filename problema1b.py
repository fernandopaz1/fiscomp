import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as spline
#from scipy.interpolate.InterpolatedUnivariateSpline import derivative as splineder
from subprocess import call



#Punto a

datos=np.loadtxt('distribucion_perco',dtype=float)



iteraciones=27000
a=len(datos[:,1])/iteraciones

dim=64

p=np.linspace(0.01,0.99,a)
cuento_precolaciones=np.zeros(len(p))


for i in range(0,len(p)):
	for k in range(0,iteraciones):
		cuento_precolaciones[i]=cuento_precolaciones[i]+datos[k+i*iteraciones,1]
	
	
cuento_precolaciones=cuento_precolaciones/iteraciones

#spl_perco=spline(p,cuento_percolaciones)
	

plt.figure(1)
line1, = plt.plot(p,cuento_precolaciones)
plt.show(block=True)


