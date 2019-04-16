import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as spline
from subprocess import call




datos=np.loadtxt('dim_fractal',dtype=float)








l=datos[:,0]
m=datos[:,2]

P=np.zeros(len(m))

for i in range(0,len(l)):
	P[i]=m[i]/(l[i]*l[i])		



plt.figure(1)
plt.scatter(l,np.log10(P))
plt.show(block=True)


