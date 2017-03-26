#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:14:52 2017

@author: prasanna
"""
import numpy
from matplotlib import rcParams, cm
from matplotlib import pyplot
nx = 41
ny = 41

l = 1.
h = 1.

dx = l/(nx-1)
dy = h/(ny-1)

l1_target = 1e-6

def L1norm(new, old):
    norm = numpy.sum(numpy.abs(new-old))
    return norm
def stokes_IG(nx, ny,l,h):
    x  = numpy.linspace(0,l,nx)
    y  = numpy.linspace(0,h,ny)
    X,Y = numpy.meshgrid(x,y)
    om_i=numpy.ones((ny,nx))
    om_i[0,1:-1]=0
    om_i[1:-1,0]=0
    om_i[1:-1,-1]=0
    chi_i=numpy.zeros((ny,nx))
    
    
    return X, Y, x, y, om_i,chi_i, dx, dy
    
def stokes_2d(om,chi ,nx,ny, dx, dy, l1_target):
    l1_norm = 1
    l1_norm2=1
    iterations = 0
    l1_conv = []
    l1_conv2 = []
    
    while l1_norm and l1_norm2 > l1_target:

        omd = om.copy()
        chid= chi.copy()
        
        
        om[1:-1,1:-1] = 0.25*(omd[2:,1:-1]+omd[:-2,1:-1]+omd[1:-1,2:]+omd[1:-1,:-2])
        om[-1,:]=(-3/dy)+(3.5*chi[-1,:]-4*chi[-2,:]+0.5*chi[-3,:])/(dy**2)
        om[0,:]=(3.5*chi[0,:]-4*chi[1,:]+0.5*chi[2,:])/(dy**2)
        om[:,0]=(3.5*chi[:,0]-4*chi[:,1]+0.5*chi[:,2])/(dy**2)
        om[:,-1]=(3.5*chi[:,-1]-4*chi[:,-2]+0.5*chi[:,-3])/(dy**2)
        chi[1:-1,1:-1] = 0.25*(chid[2:,1:-1]+chid[:-2,1:-1]+chid[1:-1,2:]+chid[1:-1,:-2]+dx**2*om[1:-1,1:-1])
        
        
        
        
        l1_norm=L1norm(om,omd)
        l1_norm2=L1norm(chi,chid)
        iterations+=1
        l1_conv.append(l1_norm)
        l1_conv2.append(l1_norm2)
        print(l1_norm)
        print(l1_norm2)
    print('Number of Jacobi iterations: {0:d}'.format(iterations))
    return om , chi , l1_conv , l1_conv2

X, Y, x, y, om_i,chi_i, dx, dy= stokes_IG(nx, ny, l, h)

omf , chif , lcon1 , lcon2 = stokes_2d(om_i,chi_i,nx,ny,dx,dy,l1_target)
pyplot.figure(figsize=(8,8))
pyplot.contourf(X,Y,chif,10,cmap=cm.viridis)
    

    