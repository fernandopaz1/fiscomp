import numpy as np
import math as mt
import matplotlib.pyplot as plt




datos=np.loadtxt('datos_1b',dtype=float)


dim=64



p=datos[:,0]

def pc_med(myList = [], *args):

    cuento_precolaciones=myList
    
    for i in range(0,len(p)) :
        	if(cuento_precolaciones[i]>0.5):		#Este indice es el del primer elemento mayor a 0.5
        		break		
    
    
    
    a=(cuento_precolaciones[i]-cuento_precolaciones[i-1])/(p[i]-p[i-1])
    b=cuento_precolaciones[i-1]					#La interpolacion es a*x+b
    
    def interpol(x,a,b):
    	f=a*(x-p[i-1])+b
    	return f							#La inversa si evaluo en 0.5 me deberia dar pc
    def invers(x,a,b):
    	inver=(x-b)/a+p[i-1]
    	return inver							#La inversa si evaluo en 0.5 me deberia dar pc
    
    pc=invers(0.5,a,b)
    return pc,a,b,i

pc,a,b,i=pc_med(datos[:,3])

def interpol(x,a,b):
    	f=a*(x-p[i-1])+b
    	return f	
						#La inversa si evaluo en 0.5 me deberia dar pc

x=np.linspace(-0.03+pc,0.03+pc,100)
y=np.zeros(len(x))
for j in range(0,len(x)):
	y[j]=interpol(x[j],a,b)

linea1=[0,pc]             #Horizontal
linea2=[0,0.5]		#vertical

print("La porbabilidad critica es:   ", pc)

size=5

L=np.zeros(5)

for k in range(0,5):
		L[k]=dim+k*(128-dim)//5;
	

lab=''

for i in range(2,6):
    pc,a,b,j=pc_med(datos[:,i])
    tam=int(L[i-1])
    lab =lab + 'L= {}; pc = {}'.format(tam,pc)

plt.figure(1)
line1 = plt.scatter(p,datos[:,2],s=size,label=lab[0:30])
plt.plot(x,y)
line2 = plt.scatter(datos[:,0],datos[:,3],s=size,label=lab[30:60])
line3 = plt.scatter(datos[:,0],datos[:,4],s=size,label=lab[60:91])
line4 = plt.scatter(datos[:,0],datos[:,5],s=size,label=lab[91:122])
plt.plot(linea1,0.5*np.ones(len(linea1)))
plt.plot(pc*np.ones(len(linea2)),linea2)
plt.xlabel('p')
plt.ylabel('Distribucion de probabilidad')
axes = plt.gca()
axes.set_xlim([0.55,0.63])
#axes.set_ylim([0.55,0.65])
legend1 = plt.legend(handles=[line1,line2,line3,line4], loc='Best')
plt.show(block=True)


