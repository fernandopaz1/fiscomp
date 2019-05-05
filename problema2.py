import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as spline
from subprocess import call
import matplotlib.ticker as mticker




datos=np.loadtxt('dim_fractal_amplio',dtype=float)


l=datos[:,0]

m=datos[:,1]
P=np.zeros(len(m))
for i in range(1,len(l)):
	P[i]=m[i]/(l[i]*l[i])		

colores=['violet','green','black','blue','orange','red']
lab=list()
reg_lineal=10
xi=np.zeros(len(datos[0,1:len(datos[0,:])]))
p_inf=np.zeros(len(datos[0,1:len(datos[0,:])]))
D=91/48
plt.figure(3)
for j in range(1,6):
    m=datos[:,j]
    P=np.zeros(len(m))
    rho=np.zeros(len(m))
    rho_der=np.zeros(len(m)-1)
    for i in range(1,len(l)):
        P[i]=(m[i]/(l[i]*l[i]))
        rho[i]=P[i]/(l[i]**(2-D))
        
    for i in range(1,len(l)):
        rho_der[i-1]=(rho[i]-rho[i-1])
    const=min(abs(rho_der))
    indice_const=np.where(abs(rho_der)==const)[0][0]+1
    
    
    
    p1=np.sum(rho[indice_const-30:indice_const+10])/len(rho[indice_const-30:indice_const+10])
    p2=np.polyfit(np.log(l[1:reg_lineal]),(rho[1:reg_lineal]),1)
    if(j!=3):
        col=colores[j]
        delta_p=abs(datos[0,j]-0.5927171794445764)
        lab='$|p-p_c| = {}$'.format('%.3f' %(delta_p))
        x_aux2=np.linspace(np.exp((p1-p2[1])/p2[0]),190,2)
        plt.plot(x_aux2,p1*np.ones(len(x_aux2)))
        x_aux=np.linspace(l[1],np.exp((p1-p2[1])/p2[0]),100)
        plt.plot(x_aux,np.polyval(p2,np.log(x_aux)),color=col) 
        line1=plt.scatter(l[1:len(rho)],(rho[1:len(rho)]),s=2,color=col,label=lab)
        plt.xscale('log')
        ax=plt.gca()
        ax.set_xticks((5, 10, 20, 50, 100, 200))
        ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
        ax.get_xaxis().set_minor_formatter(mticker.NullFormatter())
    
    xi[j-1]=np.exp((p1-p2[1])/p2[0])
    p_inf[j-1]=p1  
plt.xlabel('$L$')
h=plt.ylabel('$\\tilde{\\rho}(L)$')
h.set_rotation(0)
plt.legend()
plt.show(block=True)

x_nu=abs(datos[0,1:len(datos[0,:])]-0.5927171794445764)

x_nu=np.delete(x_nu,2)
xi=np.delete(xi,2)
p_inf=np.delete(p_inf,2)

p3=np.polyfit(np.log(x_nu),np.log(xi),1)

p4=np.polyfit(np.log(x_nu),np.log(p_inf),1)

size=2
plt.figure(2)
line1 = plt.scatter((x_nu),np.log(xi),s=size)
line2 = plt.plot((x_nu),np.polyval(p3,np.log(x_nu)))
plt.xlabel('$p-p_c$')
plt.ylabel('$\\xi$')
#plt.xscale('log')
#plt.yscale('log')
plt.show(block=True)

plt.figure(4)
line1 = plt.scatter(x_nu,p_inf,s=size)
plt.xlabel('$p-p_c$')
plt.ylabel('$P_\\infty$')
#plt.xscale('log')
plt.yscale('log')
#legend1 = plt.legend(handles=[line1,line2,line3,line4], loc='Best')
plt.show(block=True)



"""

Calculo de la dimensión factal utilizando 
un ajuste lineal en log(m) vs log(L)

"""

rango=30

lab=''
acum=0
for i in range(2,6):
    D=np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,i]),1)[0]
    acum=acum+D
    lab =lab + 'L = {}; D = {}'.format(int(l[i]),'%.5f' % D)


size=2

plt.figure(1)
line1 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,2]),s=size,label=lab[0:18])
line1a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,2]),1),np.log(l[2:101])))

line2 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,3]),s=size,label=lab[18:36])
line2a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,3]),1),np.log(l[2:101])))

line3 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,4]),s=size,label=lab[36:54])
line3a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,4]),1),np.log(l[2:101])))

line4 = plt.scatter(np.log(l[2:101]),np.log(datos[2:101,5]),s=size,label=lab[54:72])
line4a= plt.plot(np.log(l[2:101]),np.polyval(np.polyfit(np.log(l[2:rango]),np.log(datos[2:rango,5]),1),np.log(l[2:101])))

plt.xlabel('Log(L)')
plt.ylabel('Log(M)')
#axes = plt.gca()
#axes.set_xlim([0.55,0.63])
#axes.set_ylim([0.55,0.65])
legend1 = plt.legend(handles=[line1,line2,line3,line4], loc='Best')
plt.show(block=True)

print('La dimension fratal es: ', acum/4)


D_nueva=acum/4

