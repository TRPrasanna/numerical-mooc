#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:12:44 2017

@author: prasanna
"""

import sympy
from sympy import init_printing
init_printing()
from sympy.utilities.lambdify import lambdify
x = sympy.symbols('x')
a= sympy.cos(x)**2*sympy.sin(x)**3/(4*x**5*sympy.exp(x))
axprime=a.diff(x)
ax= lambdify(x,axprime)
