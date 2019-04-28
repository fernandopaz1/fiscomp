#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:26:50 2019

@author: paz
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as spline
from subprocess import call



#datos=np.loadtxt('masa',dtype=float)

datos=np.loadtxt('masa',dtype=float)

long=int(len(datos[:,0])/10)


#dat64=datos[0:long,:]
#dat70=datos[long:2*long,:]
#dat76=datos[2*long:3*long,:]
#dat83=datos[3*long:4*long,:]
#dat89=datos[4*long:5*long,:]
#dat96=datos[5*long:6*long,:]
#dat102=datos[6*long:7*long,:]
#dat108=datos[7*long:8*long,:]
#dat115=datos[8*long:9*long,:]
#dat121=datos[9*long:10*long,:]


L=[64,70,76,83,89,96,102,108,115,121]



plt.figure(1)
for i in range(0,9):
    lab ='L = {}'.format(L[i])
    plt.scatter(datos[i*long:(i+1)*long,1],(datos[i*long:(i+1)*long,2])/(L[i]*L[i]),s=2,label=lab)
plt.xlabel('p')
plt.ylabel('$P_{\infty}(L)$')
legend1 = plt.legend(loc='Best')
plt.show(block=True)

