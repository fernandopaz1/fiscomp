import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



datos=np.loadtxt('distribucion_fragmentos', delimiter=" ")

nat=np.zeros(len(datos[1,:]))

for i in range(0,len(datos[1,:])):
	nat[i]=i


plt.scatter(np.log(nat),np.log(datos[1,:]))
#plt.xscale("log")
#plt.yscale("log")
plt.show()

