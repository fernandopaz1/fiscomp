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
#x=(natural[1450:1700])
#y=(argum[1450:1700])
x=np.log(natural)
y=np.log(argum)
var1=x[1500:1700]
var2=y[1500:1700]
plt.figure(4)
plt.scatter(x,y,s=size)
p2=np.polyfit(var1,var2,1)
plt.plot(var1,p2[0]*var1+p2[1]*np.ones(len(var1)))
#plt.xscale('log')
#plt.yscale('log')
plt.show()


s0=64**2


font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 11,
        }

indice_prob=866
a=np.ones(len(datos[:,0]))
pc64=0.59256
pc64=datos[indice_prob,0]
b=0.334
plt.figure(5)
line1 = plt.scatter((datos[:,0]-pc64*a),datos[:,1]/datos[indice_prob,1],s=size,label='s=1')
line2 = plt.scatter((datos[:,0]-pc64*a)*(2**b),datos[:,2]/datos[indice_prob,2],s=size,label='s=2')
line3 = plt.scatter((datos[:,0]-pc64*a)*(3**b),datos[:,3]/datos[indice_prob,3],s=size,label='s=3')
line4 = plt.scatter((datos[:,0]-pc64*a)*(4**b),datos[:,4]/datos[indice_prob,4],s=size,label='s=4')
line5 = plt.scatter((datos[:,0]-pc64*a)*(5**b),datos[:,5]/datos[indice_prob,5],s=size,label='s=5')
line6 = plt.scatter((datos[:,0]-pc64*a)*(6**b),datos[:,6]/datos[indice_prob,6],s=size,label='s=6')
line7 = plt.scatter((datos[:,0]-pc64*a)*(7**b),datos[:,7]/datos[indice_prob,7],s=size,label='s=7')
line8 = plt.scatter((datos[:,0]-pc64*a)*(8**b),datos[:,8]/datos[indice_prob,8],s=size,label='s=8')
line9 = plt.scatter((datos[:,0]-pc64*a)*(9**b),datos[:,9]/datos[indice_prob,9],s=size,label='s=9')
line10 = plt.scatter((datos[:,0]-pc64*a)*(10**b),datos[:,10]/datos[indice_prob,10],s=size,label='s=10')
line11 = plt.scatter((datos[:,0]-pc64*a)*(11**b),datos[:,11]/datos[indice_prob,11],s=size,label='s=11')
line12 = plt.scatter((datos[:,0]-pc64*a)*(12**b),datos[:,12]/datos[indice_prob,12],s=size,label='s=12')
line13 = plt.scatter((datos[:,0]-pc64*a)*(13**b),datos[:,13]/datos[indice_prob,13],s=size,label='s=13')
line14 = plt.scatter((datos[:,0]-pc64*a)*(15**b),datos[:,15]/datos[indice_prob,15],s=size,label='s=15')
line15= plt.scatter((datos[:,0]-pc64*a)*(14**b),datos[:,14]/datos[indice_prob,14],s=size,label='s=14')
plt.xlabel('z')
plt.ylabel('$\\frac{<ns(p)>}{<ns(p_c)>}$')
#plt.yscale('log')
plt.text(-0.9, 5.5, '$\\sigma=0.334$', fontdict=font)
legend1 = plt.legend(handles=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15], loc='Best')
plt.show()

maxim=np.zeros(15)
naturales=np.zeros(15)

b=0.334
for i in range(1,16):
    a=max(datos[:,i])
    indice_max=int(np.where(datos[:,i] == a)[0][0])
    maxim[i-1]=(datos[indice_max,0]-pc64)*(i**b)
    naturales[i-1]=i-1


rango=max(maxim)-min(maxim) 
labe ='rango = {}'.format('%.2f' %rango)   
plt.figure(7)
line1 = plt.scatter(naturales,maxim,label='$\\epsilon_{smax}$')
legend = plt.legend(handles=[line1], loc='Best')
plt.xlabel('s')
plt.ylabel('$\\epsilon_s$')
#plt.text(0, -0.38, 'Tolerancia= {}'.format('%.2f' %rango), fontdict=font)
plt.show()




print('El coeficiente $\\sigma$ es: ',b)


indice_prob=866
a=np.ones(len(datos[:,0]))
pc64=0.59256
pc64=datos[indice_prob,0]
b=0.334
plt.figure(6)
line2 = plt.scatter((datos[:,0]-pc64*a)*(41**b),(datos[:,41]/datos[indice_prob,41]),s=size,label='s=41')
line3 = plt.scatter((datos[:,0]-pc64*a)*(42**b),(datos[:,42]/datos[indice_prob,42]),s=size,label='s=42')
line4 = plt.scatter((datos[:,0]-pc64*a)*(43**b),(datos[:,43]/datos[indice_prob,43]),s=size,label='s=43')
line5 = plt.scatter((datos[:,0]-pc64*a)*(44**b),(datos[:,44]/datos[indice_prob,44]),s=size,label='s=44')
line6 = plt.scatter((datos[:,0]-pc64*a)*(45**b),(datos[:,45]/datos[indice_prob,45]),s=size,label='s=45')
line7 = plt.scatter((datos[:,0]-pc64*a)*(46**b),(datos[:,46]/datos[indice_prob,46]),s=size,label='s=46')
line8 = plt.scatter((datos[:,0]-pc64*a)*(47**b),(datos[:,47]/datos[indice_prob,47]),s=size,label='s=47')
line9 = plt.scatter((datos[:,0]-pc64*a)*(48**b),(datos[:,48]/datos[indice_prob,48]),s=size,label='s=48')
line10 = plt.scatter((datos[:,0]-pc64*a)*(49**b),(datos[:,49]/datos[indice_prob,49]),s=size,label='s=49')
line11 = plt.scatter((datos[:,0]-pc64*a)*(50**b),np.log(datos[:,50]/datos[indice_prob,50]),s=size,label='s=50')
plt.xlabel('z')
plt.ylabel('$\\frac{<ns(p)>}{<ns(p_c)>}$')
##axes = plt.gca()
##axes.set_xlim([-0.8,0])
plt.gca().set_ylim(0.0001, 10)
#plt.gca().set_xlim(0.0001, 10)
plt.yscale('log')
legend1 = plt.legend(handles=[line2,line3,line4,line5,line6,line7,line8,line9,line10], loc='Best')
plt.show()



pc128=0.5926
pc64=0.59256
pc=pc64
m1=np.zeros(len(datos[:,0]))
m0=np.zeros(len(datos[:,0]))
s=np.zeros(len(datos[0,:]))
for j in range(0,len(datos[0,:])):
    if(j<70):
        s[j]=j
s_cuad=s**2

m2=np.zeros(len(datos[:,0]))
for i in range(0,len(datos[:,0])):
    m2[i]=np.sum(datos[i,:]*s_cuad)#max(datos[i,:])
    m1[i]=np.sum(datos[i,:]*s)#/max(datos[i,:])
    m0[i]=np.sum(datos[i,:])/max(datos[i,:])
    

#m2=m1/m0
#m2=m0    
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
alfa=2-(tau-1)/(sigma)
beta=nu*(d-D)
gamma=(3-t)/sigma