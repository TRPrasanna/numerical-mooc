#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:08:54 2017

@author: prasanna
"""
import numpy
from matplotlib import pyplot
import matplotlib.cm as cm
from matplotlib import animation
from JSAnimation.IPython_display import display_animation
#initial conditions
n = 192

Du, Dv, F, k = 0.00016, 0.00008, 0.035, 0.065 # Bacteria 1 

dh = 5/(n-1)

T = 8000

dt = .9 * dh**2 / (4*max(Du,Dv))

nt = int(T/dt)
x = numpy.linspace(0,5,n)
y = numpy.linspace(0,5,n)

#/initial conditions

uvinitial = numpy.load('./uvinitial.npz')
U = uvinitial['U']
V = uvinitial['V']

'''fig = pyplot.figure(figsize=(8,5))
pyplot.subplot(121)
pyplot.imshow(U, cmap = cm.RdBu)
pyplot.xticks([]), pyplot.yticks([]);
pyplot.subplot(122)
pyplot.imshow(V, cmap = cm.RdBu)
pyplot.xticks([]), pyplot.yticks([]);'''

def ftcs(u ,v ,nt ,dt ,dh ,Du ,Dv,F ,k ):
    um=numpy.zeros((84,192,192))
    i=0
    j=0
    for n in range(nt):
        
        un=u.copy()
        vn=v.copy()
        u[1:-1,1:-1]=un[1:-1,1:-1]+dt*(Du/dh**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[:-2,1:-1]+un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,:-2])-un[1:-1,1:-1]*vn[1:-1,1:-1]**2+F*(1-un[1:-1,1:-1]))
        v[1:-1,1:-1]=vn[1:-1,1:-1]+dt*(Dv/dh**2*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[:-2,1:-1]+vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,:-2])+un[1:-1,1:-1]*vn[1:-1,1:-1]**2-vn[1:-1,1:-1]*(F+k))
        u[0,:]=u[1,:]
        u[-1,:]=u[-2,:]
        u[:,0]=u[:,1]
        u[:,-1]=u[:,-2]
        v[0,:]=v[1,:]
        v[-1,:]=v[-2,:]
        v[:,0]=v[:,1]
        v[:,-1]=v[:,-2]#nuemann boundaries
        if i%100==0:
          um[j,:,:]=u
          j+=1
          #print(j)
        i+=1
    return um
unew=ftcs(U,V,nt,dt,dh,Du,Dv,F,k)



fig = pyplot.figure(figsize=(8,5), dpi=72)
img = pyplot.imshow(unew[0],cmap = cm.RdBu)
def animate(data):
    img.set_array(data)
    return img,

anim = animation.FuncAnimation(fig, animate, frames=unew, interval=85)
display_animation(anim, default_mode='once') #run in jupyter-notebook

        
         
    
    