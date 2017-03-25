#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:05:16 2017

@author: prasanna
"""

import numpy
import matplotlib
burnrate=numpy.zeros(1001)
t=numpy.linspace(0,100,1001)
burnrate[:501]=20
dt=0.1
g=9.81
ve=325
rho=1.091
a=numpy.pi*0.5**2
C_d=0.15
ms=50

#matplotlib.pyplot.plot(t,burnrate)
mp= 100 - burnrate * t
mp[51:]=0
v=numpy.zeros(1001)
h=numpy.zeros(1001)
h[0]=0
v[0]=0
for i in range(0,999):
    v[i+1]=v[i]+dt*(-g+(burnrate[i]*ve-0.5*rho*numpy.square(v[i])*a*C_d)/(ms+mp[i]))
    h[i+1]=h[i]+v[i]*dt

    
    