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
from IPython.display import HTML
#initial conditions
n = 192

Du, Dv, F, k = 0.00016, 0.00008, 0.035, 0.065 # Bacteria 1 

dh = 5/(n-1) #dx=dy=dh

T = 8000 # time=8000 seconds

dt = .9 * dh**2 / (4*max(Du,Dv)) #time step size

nt = int(T/dt) #number of time steps

x = numpy.linspace(0,5,n) # x mesh
y = numpy.linspace(0,5,n) # y mesh

#/initial conditions

uvinitial = numpy.load('./uvinitial.npz') #loads initial u and v concentrations from working directory
U = uvinitial['U']
V = uvinitial['V']


def ftcs_new(nt,u ,v ,dt ,dh ,Du ,Dv,F ,k):
    '''Generate U and V (bacteria concentrations)of Gray Scott model for one time step 
       Assumes dx=dy=dh
       
       Parameters:
       ----------
       nt  : int
          number of time steps/ nth time step for anim function
       u   : 2d array of floats
          concentration of species u
       v   : 2d array of floats
          concentration of species v
       dt  : float
          size of time step
       dh  : float
          mesh spacing
       Du  : float
          rate of diffusion os species u
       Dv  : float
          rate of diffusion of species v
       F   : float
          term in feed rate
       k : float
          term in kill rate
          
       Returns :
       -------
       img : image of colourmap RdBu
           snapshot of concentration of species u at current time step
       
       '''
    un=u 
    vn=v  # un and vn point to U and V concentrations
    u[1:-1,1:-1]=un[1:-1,1:-1]+dt*(Du/dh**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[:-2,1:-1]+un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,:-2])-un[1:-1,1:-1]*vn[1:-1,1:-1]**2+F*(1-un[1:-1,1:-1]))
    v[1:-1,1:-1]=vn[1:-1,1:-1]+dt*(Dv/dh**2*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[:-2,1:-1]+vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,:-2])+un[1:-1,1:-1]*vn[1:-1,1:-1]**2-vn[1:-1,1:-1]*(F+k))
    u[0,:]=u[1,:]#nuemann boundaries
    u[-1,:]=u[-2,:]
    u[:,0]=u[:,1]
    u[:,-1]=u[:,-2]
    v[0,:]=v[1,:]
    v[-1,:]=v[-2,:]
    v[:,0]=v[:,1]
    v[:,-1]=v[:,-2]#/nuemann boundaries
 
    img=pyplot.imshow(u,cmap=cm.RdBu)
       
    return img
    

fig = pyplot.figure(figsize=(8,5));
anim =animation.FuncAnimation(fig,ftcs_new,frames=nt,fargs=(U ,V ,dt ,dh ,Du ,Dv,F ,k),interval=10)
HTML(anim.to_html5_video())    
# pyplot.show()    
    






        
         
    
    