#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:55:04 2017

@author: prasanna
"""

import numpy
#from matplotlib import pyplot
vmax=136.0 #case 1 : 80 , case 2:136
L=11.0
rhomax=250.0
nx=51
dt=0.001
##case 1## !! case 2 = 20 instead of 10 !!
x = numpy.linspace(0,L,nx)
rho0 = numpy.ones(nx)*20.0
rho0[10:20] = 50.0
#/case1##
time= 0.1 # in hours
rho=rho0.copy()
rho_req=numpy.zeros(nx)
m=0
ti=numpy.linspace(0,time,int(time/dt)+1)
for t in ti:
    rho[1:]=rho[1:]-(vmax*dt/0.22)*((rho[1:]*(1-rho[1:]/rhomax))-(rho[:-1]*(1-rho[:-1]/rhomax)))
    if (t==0.05):
        rho_req=rho.copy()
        m+=1

rho_3m=rho_req.copy()
rho_0m=rho0
rho_6m=rho.copy()
v_0=vmax*(1-rho_0m/rhomax)
v_3=vmax*(1-rho_3m/rhomax)
v_6=vmax*(1-rho_6m/rhomax)
