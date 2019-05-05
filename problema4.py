import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


datos=np.loadtxt('distribucion_fragmentos', delimiter=" ")


size=2
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


b=0.334    #Parametro para ajustar sigma


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

plt.xlabel('z')
plt.ylabel('$\\frac{<ns(p)>}{<ns(p_c)>}$')

ax=plt.gca()
ax.get_yaxis().set_major_formatter(mticker.ScalarFormatter())
ax.get_yaxis().set_minor_formatter(mticker.NullFormatter())

plt.gca().set_ylim(0.0001, 10)
plt.yscale('log')
legend1 = plt.legend(handles=[line2,line3,line4,line5,line6,line7,line8,line9,line10], loc='Best')
plt.show()

