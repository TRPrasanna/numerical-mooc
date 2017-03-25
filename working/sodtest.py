#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:20:08 2017

@author: prasanna
"""
from matplotlib import pyplot
import numpy
x=numpy.linspace(-10,10,81)
rho=numpy.zeros_like(x)
u=numpy.zeros_like(x)
p=numpy.zeros_like(x)
nx = 81
dx = .25
dt = .0002   
gamma = 1.4
rho[:40]=1
rho[40:]=0.125
p[:40]=100000
p[40:]=10000
#uvec=numpy.empty((3,nx))
u_init=numpy.array([rho,rho*u,((p/.4)+(0.5*rho*u**2))])
def computeF(u,gamma):
    
    flux = numpy.array([u[1,:],((u[1,:]**2)/u[0,:])+(gamma-1)*(u[2,:]-0.5*((u[1,:]**2)/u[0,:])),(u[1,:]/u[0,:])*(u[2,:]+(gamma-1)*(u[2,:]-0.5*((u[1,:]**2)/u[0,:])))])
    return flux

def rhictmeyer(uinit,dx,dt,gamma):
    uvector=uinit.copy()
    uhalf=uinit.copy()
    unew=numpy.zeros((3,nx))
    for t in range(1,51):
        
        F=computeF(uvector,gamma)
        uhalf[:,:-1]=0.5*(uvector[:,1:]+uvector[:,:-1])-0.5*dt/dx*(F[:,1:]-F[:,:-1])
        F=computeF(uhalf,gamma)
        unew[:,1:]=uvector[:,1:]-dt/dx*(F[:,1:]-F[:,:-1])
        unew[:,0]=uvector[:,0]
        uvector=unew.copy()
    return unew
variables=rhictmeyer(u_init,dx,dt,gamma)
pyplot.plot(x,0.4*(variables[2,:]-0.5*variables[1,:]**2/variables[0,:])) #pressure
pyplot.plot(x,variables[1,:]/variables[0,:]) #velocity
pyplot.plot(x,variables[0,:]) #density

        
        
    
    