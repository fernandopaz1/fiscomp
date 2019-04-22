import numpy as np
import math as mt
import matplotlib.pyplot as plt
from subprocess import call



#Punto a

datos=np.loadtxt('pc')

iteraciones=27000




dim=np.zeros(int(len(datos[:,0])/iteraciones))


for i in range(0,len(dim)):
	dim[i]=datos[i*iteraciones,0]


p_l=np.zeros(len(dim))
p_cuad_l=np.zeros(len(dim))
sigma=np.zeros(len(dim))

for i in range(0,len(dim)):
	for k in range(0,iteraciones):
		p_l[i]=p_l[i]+datos[k+i*iteraciones,1]
		p_cuad_l[i]=p_cuad_l[i]+datos[k+i*iteraciones,2]
p_l=p_l/iteraciones
p_cuad_l=p_cuad_l/iteraciones


for i in range(0,len(dim)):
	sigma[i]= np.sqrt(p_cuad_l[i] - (p_l[i])*(p_l[i]))



###########################################################################
#
#			pc(L) vs sigma
#			ajuste ---->  pc(inf)
#
##########################################################################
nro_ptos=10


sigma_fit=np.zeros(nro_ptos)
p_l_fit=np.zeros(nro_ptos)

for i in range(0,nro_ptos):
	sigma_fit[i]=sigma[i+len(sigma)-nro_ptos]
	p_l_fit[i]=p_l[i+len(sigma)-nro_ptos]
	
fit_coef=np.polyfit(sigma_fit, p_l_fit, 1, rcond=None, full=True, w=None, cov=False)

def fit_lineal(x):
	f=x*fit_coef[0][0]+fit_coef[0][1]
	return f


f=np.zeros(len(dim))
pc_inf=fit_coef[0][1]


for i in range(0,len(dim)):
	f[i]=fit_lineal(sigma[i])	
	
print("El valor de pc es: ", fit_coef[0][1])

plt.figure(2)
line1 = plt.scatter(sigma,p_l,label='$p_{c}(L)$',marker='^')
line2, = plt.plot(sigma,f,label='Ajuste lineal',linestyle='--')
plt.xlabel('$\sigma$')
plt.ylabel('$p_{c}(L)$')
axes = plt.gca()
#axes.set_xlim([xmin,xmax])
axes.set_ylim([0.55,0.65])
legend1 = plt.legend(handles=[line1,line2], loc=1)
plt.show(block=True)




###########################################################
#
#		Ajusta y grafica para sacar \nu		
#
###########################################################

puntos=5

dim_fit=np.zeros(puntos)
p_l_fit2=np.zeros(puntos)

for i in range(0,puntos):
	dim_fit[i]=dim[i]
	p_l_fit2[i]=p_l[i]
	
fit_coef2=np.polyfit(np.log(dim_fit), np.log(np.absolute(pc_inf*np.ones(len(dim_fit))-p_l_fit2)), 1, rcond=None, full=False, w=None, cov=False)

def fit_lineal(x):
	f2=x*fit_coef2[0]+fit_coef2[1]
	return f2


f2=np.zeros(len(dim))
nu=fit_coef2[0]

print("El exponente $\{nu}$ es:  ", -1/nu)

for i in range(0,len(dim)):
	f2[i]=fit_lineal(np.log(dim[i]))	



plt.figure(1)
plt.scatter(np.log(dim),np.log(np.absolute(pc_inf*np.ones(len(dim))-p_l)))
plt.plot(np.log(dim),f2)
plt.show(block=True)


##############################################################################

