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
rang=80
#rang=len(datos[1,:])
size=2
#rango_min=1  #para 6
#rang=10     #para 6

x=np.log(range(rango_min,rang))
for i in range(0,probas):
    y=np.log(datos[i,rango_min:rang])
    p=np.polyfit(x,y,1)
    taus[i]=p[0]
    chi_squared[i]=np.sum((np.polyval(p,x)-y)**2)
    
indice=886    #para 64
frag=4000    #para 64    
#indice=400    #para 6
#frag=35
#rang=10
plt.figure(1)
x=np.log(range(rango_min,rang))
y=np.log(datos[indice,rango_min:rang])
p=np.polyfit(x,y,1)
line1 = plt.scatter(np.log(range(1,frag)),np.log(datos[indice,1:frag]),s=size,label='ns')
line2, = plt.plot(x,np.polyval(p,x),label='Ajuste lineal',color='red')
plt.xlabel('log(s)')
plt.ylabel('log(ns)')
legend1 = plt.legend(handles=[line1,line2], loc='Best')
plt.show()

plt.figure(2)
line1 = plt.scatter(datos[:,0],(chi_squared),s=size,label='Error cuadrático medio')
legend1 = plt.legend(handles=[line1], loc='Best')
plt.xlabel('p')
plt.ylabel('${\\chi}^2$')
plt.yscale('log')
plt.show()






np.min(chi_squared[300:len(chi_squared)])
indice_optimo=np.where(chi_squared == min(chi_squared[300:len(chi_squared)]))[0][0]
pc_64=datos[indice_optimo,0]
tau=taus[indice_optimo]



plt.figure(3)
line1 = plt.scatter(datos[300:len(chi_squared),0],taus[300:len(chi_squared)],s=size,label='Pendiente')
legend1 = plt.legend(handles=[line1], loc='Best')
plt.xlabel('p')
plt.ylabel('$\\tau$')
plt.show()

print('El valor de taus es:  ',tau)


pc64=datos[indice_optimo,0]


pmax=np.zeros(len(datos[0,:])-1)

natural=np.zeros(len(pmax))
for i in range(1,len(pmax)):
    a=max(datos[1:len(datos[:,0]),i])
    ind_max=int(np.where(datos[:,i] == a)[0][0])
    pmax[i]=datos[ind_max,0]
    natural[i]=i+1;



argum=(pmax-pc64*np.ones(len(pmax)))+10
fin=len(argum)
x=np.log(natural)
y=np.log(argum)
var1=x[1500:1700]
var2=y[1500:1700]
plt.figure(4)
plt.scatter(x,y,s=size)
p2=np.polyfit(var1,var2,1)
plt.plot(var1,p2[0]*var1+p2[1]*np.ones(len(var1)))
plt.show()

"""
###############################################################
#
#                       Ajuste considerando q0
#
################################################################
"""


ns=lambda tpl,x : -tpl[0]*x+np.log(tpl[1]/sp.zeta(tpl[0]-1))

def ErrorFunc(tpl,x,y):
    return ns(tpl,x)-y





x=np.log(range(rango_min,rang))
for i in range(0,probas):
    y=np.log(datos[i,rango_min:rang])
    p=np.polyfit(x,y,1)
    tplInitial1=(2.041, p[0])
    tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x,y),maxfev=1000)
    taus[i]=tplFinal1[0]
    chi_squared[i]=np.sum(ErrorFunc(tplFinal1,x,y)**2)
    taus[i]=p[0]
    chi_squared[i]=np.sum((np.polyval(p,x)-y)**2)


#a_min=2.0218823764752947
#b_min=11212.742548509703
a_min=2.5
b_min=6500
k=0
b=np.linspace(b_min-500,b_min+500,5000)
error_ord=np.zeros(len(b))
a=np.linspace(2.01,3,5000)
error_ord1=np.zeros(len(a))
x=np.log(range(1,20))
y=np.log(datos[indice_optimo,1:20])
while(k<30):
    for i in range(0,len(b)):
        tplInitial1=(a_min,b[i])
        p=np.polyfit(x,y,1)
        error = ErrorFunc(tplInitial1,x,y)
        error_ord[i] = sum(error**2)/len(error)
    
#    plt.figure(3)
#    plt.plot(b,error_ord)
#    plt.show()
    
    err_min=min(error_ord)
    ind_min=np.where(error_ord == err_min)[0][0]
    b_min=b[ind_min]
    b=np.linspace(b_min-500,b_min+500,5000)
    
    
    for i in range(0,len(a)):
        tplInitial1=(a[i],b_min)
        p=np.polyfit(x,y,1)
        error = ErrorFunc(tplInitial1,x,y)
        error_ord1[i] = sum(error**2)/len(error)
        
    err_min=min(error_ord1)
    ind_min=np.where(error_ord1 == err_min)[0][0]
    a_min=a[ind_min]
    
#    plt.figure(4)
#    plt.plot(a,error_ord)
#    plt.show()
    if((k+1)%5==0):
        plt.figure(4)
        plt.semilogy(b,error_ord)
        plt.show()
        plt.figure(5)
        plt.semilogy(a,error_ord1)
        plt.show()
    
    
    k=k+1
    

 


x=np.log(range(rango_min,rang))
y=np.log(datos[indice_optimo,rango_min:rang])

tplInitial1=[a_min,b_min]

plt.figure(6)
line1 = plt.scatter(np.log(range(1,frag)),np.log(datos[indice,1:frag]),s=size)
#tplFinal1,success=leastsq(ErrorFunc,tplInitial1[:],args=(x,y),maxfev=1000)
line2 = plt.plot(np.log(range(1,frag)),ns(tplInitial1,np.log(range(1,frag))))
#line3, = plt.plot(x,np.polyval(p,x))
plt.xlabel('$\\log(s)$')
plt.ylabel('$\\log(n_s)$')
legend1 = plt.legend([line1,line2], ['$n_s$','Ajuste Lineal'], loc='Best')
plt.show()

