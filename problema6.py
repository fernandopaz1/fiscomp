#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:18:06 2019

@author: paz
"""
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import scipy.special as sp
from scipy.optimize import leastsq


datos=np.loadtxt('distribucion_fragmentos', delimiter=" ")

pc64=0.59256
pc=pc64
m1=np.zeros(len(datos[:,0]))
m0=np.zeros(len(datos[:,0]))
s=np.zeros(len(datos[0,:]))
for j in range(0,len(datos[0,:])):
    if(j<78):
        s[j]=j
s_cuad=s**2

m2=np.zeros(len(datos[:,0]))
for i in range(0,len(datos[:,0])):
    m2[i]=np.sum(datos[i,:]*s_cuad)#max(datos[i,:])
    m1[i]=np.sum(datos[i,:]*s)#/max(datos[i,:])
    m0[i]=np.sum(datos[i,:])

m2=m2/m0  
plt.figure(8)    
plt.scatter((datos[0:len(m2),0]-pc)/pc,np.log(m2),s=2)    
#axes = plt.gca()
#axes.set_xlim([-0.4,0.4])
plt.show()
    
  
plt.figure(11)    
plt.scatter((datos[:,0]-pc)/pc,m2,s=2)    
#axes = plt.gca()
#axes.set_xlim([-0.4,0.4])
plt.show()

p1=np.zeros(80)
p2=np.zeros(80)
chi=np.zeros(80)
ventana1=50
paso1=2
ventana2=50
paso2=2
m2_max=max(m2)
indice_max=np.where(m2 == m2_max)[0][0]
indice_max=437  

indice_comienzo1=indice_max-25
indice_comienzo2=indice_max+25 

x=(datos[:,0]-pc)/pc
for i in range(0,80):
    inicio1=int(indice_comienzo1+paso1*i)
    fin1=int(inicio1+ventana1)
    inicio2=int(indice_comienzo2-paso2*i)
    fin2=int(inicio2-ventana2)
    p1[i]=np.polyfit(x[inicio1:fin1],np.log(m2[inicio1:fin1]),1)[0]
    p2[i]=np.polyfit(x[fin2:inicio2],np.log(m2[fin2:inicio2]),1)[0]
    chi[i]=(p2[i]+p1[i])**2

for i in range(0,len(chi)):
    if(chi[i]==0):
        chi[i]=100
chimin=min(chi)
ind_min=np.where(chi== chimin)[0][0]
p2[ind_min]
    
plt.figure(12)    
line1 = plt.scatter(range(0,80),-p1,label='$\\gamma+= {}$'.format('%.2f' %p1[ind_min]))    
line2 = plt.scatter(range(0,80),p2,label='$\\gamma-= {}$'.format('%.2f' %p2[ind_min]))  
legend1 = plt.legend(handles=[line1,line2], loc='Best')  
plt.xlabel('paso')
plt.ylabel('Pendientes')
legend1 = plt.legend(handles=[line1,line2], loc='Best')
plt.show()
    
plt.figure(13)    
line1 = plt.scatter(range(0,80),chi,label='Distancia entre puntos',s=10)    
legend1 = plt.legend(handles=[line1], loc='Best')  
plt.xlabel('paso')
plt.ylabel('$\\chi^2_\\gamma$')
plt.show()


D=91/48
nu=4/3
d=2
t=1+d/D
sigma=(nu*D)**(-1)
alfa=2-(t-1)/(sigma)
beta=nu*(d-D)
gamma=(3-t)/sigma