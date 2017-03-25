#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:40:34 2017

@author: prasanna
"""

import numpy
import matplotlib
burnrate=numpy.zeros(400001)
mp=numpy.zeros(400001)
t=numpy.linspace(0,40,400001)
burnrate[:50000]=20
dt=0.0001
g=9.81
ve=325.0
rho=1.091
a=numpy.pi*0.5**2.0
C_d=0.15
ms=50.0
h0=0
v0=0
#matplotlib.pyplot.plot(t,burnrate)
#mp= 100 - burnrate * t
#mp[51:]=0
for ii in range(0,400001):
    if ii < (5+dt)/dt:
        mp[ii]=100-20*ii*dt
    else:
        mp[ii]=0
        
    
def f(u):
    h=u[0]
    v=u[1]
    return numpy.array([v,-g+((burnrate[n]*ve)/(ms+mp[n]))-((0.5*rho*a*C_d*v*numpy.abs(v))/(ms+mp[n]))])

    
    
def euler_step(u , f ,dt):
    return u + f(u) * dt

u=numpy.empty((400001,2))
u[0]=numpy.array([h0,v0])

for n in range(400000):
    u[n+1]=euler_step(u[n],f,dt)



    
    

    
    

        