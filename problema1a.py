import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



#Punto a

datos=np.loadtxt('pc',dtype=float)
datos_chico=np.loadtxt('pc_l_chico',dtype=float)

iteraciones=27000

dim=np.zeros(len(datos[:,0])/iteraciones)
dim_chico=np.zeros(len(datos_chico[:,0])/iteraciones)


for i in range(0,len(dim)):
	dim[i]=datos[i*iteraciones,0]

for i in range(0,len(dim_chico)):
	dim_chico[i]=datos_chico[i*iteraciones,0]

p_l=np.zeros(len(dim))
p_cuad_l=np.zeros(len(dim))
masa=np.zeros(len(dim))
sigma=np.zeros(len(dim))
P_inf=np.zeros(len(dim))

p_l_chico=np.zeros(len(dim))

for i in range(0,len(dim)):
	for k in range(0,iteraciones):
		p_l[i]=p_l[i]+datos[k+i*iteraciones,1]
		p_l_chico[i]=p_l_chico[i]+datos_chico[k+i*iteraciones,1]
		p_cuad_l[i]=p_cuad_l[i]+datos[k+i*iteraciones,2]
		masa[i]=masa[i]+datos[k+i*iteraciones,4]
	
for i in range(0,len(dim_chico)):
	for k in range(0,iteraciones):
		p_l_chico[i]=p_l_chico[i]+datos_chico[k+i*iteraciones,1]
	
p_l=p_l/iteraciones
p_l_chico=p_l_chico/iteraciones
p_cuad_l=p_cuad_l/iteraciones
masa=masa/iteraciones



for i in range(0,len(dim)):
	sigma[i]= np.sqrt(p_cuad_l[i] - (p_l[i])*(p_l[i]))
	P_inf[i]=masa[i]/(dim[i]*dim[i])
	
fit_coef=np.polyfit(sigma, p_l, 1, rcond=None, full=False, w=None, cov=False)

def fit_lineal(x):
	f=x*fit_coef[0]+fit_coef[1]
	return f


f=np.zeros(len(dim))
pc_inf=fit_coef[1]


for i in range(0,len(dim)):
	f[i]=fit_lineal(sigma[i])	
	
print("El valor de pc es: ", fit_coef[1])

plt.figure(2)
plt.scatter(sigma,p_l)
plt.plot(sigma,f)
plt.show(block=True)



plt.figure(1)
plt.plot(np.log(dim_chico),np.log(np.absolute(pc_inf*np.ones(len(dim_chico))-p_l_chico)))
plt.show(block=True)


plt.figure(1)
plt.plot(np.log(dim),np.log(np.absolute(pc_inf*np.ones(len(dim))-p_l)))
plt.show(block=True)

dim_mezcla=np.append(dim_chico,dim)
p_l_mezcla=np.append(p_l_chico,p_l)




plt.figure(5)
plt.plot(np.log(dim_mezcla),np.log(np.absolute(pc_inf*np.ones(len(dim_mezcla))-p_l_mezcla)))
plt.show(block=True)


plt.figure(3)
plt.scatter(dim,sigma)
plt.show(block=True)


plt.figure(4)
plt.scatter(p_l-pc_inf*np.ones(len(p_l)),P_inf)
plt.show(block=True)
