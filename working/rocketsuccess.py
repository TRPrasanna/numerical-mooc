#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:22:52 2017

@author: prasanna
"""

import numpy
burnrate=numpy.zeros(401) 
mp=numpy.zeros(401)
t=numpy.linspace(0,40,401)
burnrate[:50]=20 #unintuitively, burn rate is 20 until 4.9 seconds, and not 5 as it would seem to appear intuitively
dt=0.1
g=9.81
ve=325.0
rho=1.091
a=numpy.pi*0.5**2.0
C_d=0.15
ms=50.0
h0=0
v0=0
for ii in range(0,401):
    if ii < (5+dt)/dt:
        mp[ii]=100-20*ii*dt
    else:
        mp[ii]=0
            
def f(u):
    v=u[1]
    return numpy.array([v,(-g+((burnrate[n]*ve)/(ms+mp[n]))-((0.5*rho*a*C_d*v*numpy.abs(v))/(ms+mp[n])))])
    
def euler_step(u , f ,dt):
    return u + f(u) * dt

u=numpy.empty((401,2))
u[0]=numpy.array([h0,v0])

for n in range(400):
    u[n+1]=euler_step(u[n],f,dt)
