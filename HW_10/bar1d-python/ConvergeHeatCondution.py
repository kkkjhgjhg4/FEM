#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convergence analysis for 2L bar element using the bar under heat conduction in practice 3.17.
Plot the element length - L2 norm cuvers in logarithm scale for both 
linear and quadratic elements, and obtain their convergence rates and the 
intercepts by linear regression.

Created on Thu Apr 30 21:05:47 2020

@author: xzhang
"""

from Bar1D import FERun
from Exact import ErrorNorm_HeatConduction

import numpy as np
import matplotlib.pyplot as plt

# Json data files for 2L element
files_2L = ("bar_3_17_2.json", "bar_3_17_4.json", "bar_3_17_8.json", "bar_3_17_16.json")    

  

# Run FE analysis for all files using 2L element
n2L = len(files_2L)
h2 = np.zeros(n2L)
L2Norm2 = np.zeros(n2L)
natural_bc_error = np.zeros(n2L)
for i in range(n2L):
    FERun(files_2L[i])

    # Calculate error norms for convergence study
    h2[i], L2Norm2[i], natural_bc_error[i] = ErrorNorm_HeatConduction()

'''
# plot the element length - error norm curve in logarithmic scale
fig,(axs) = plt.subplots(2,2)
plt.tight_layout()

axs[0,0].set_title('Linear element', fontsize=9); 
axs[0,0].set_ylabel('L_2 error', fontsize=8)
axs[0,0].xaxis.set_tick_params(labelsize=7)
axs[0,0].yaxis.set_tick_params(labelsize=7)
axs[0,0].set_xscale('log')
axs[0,0].set_yscale('log')
axs[0,0].plot(h2,L2Norm2)

plt.show()'''


fig, axs = plt.subplots(2, 1, figsize=(8, 10)) 

# L2-Norm error and h figure
axs[0].set_title('Linear element L2 error in logarithmic scale', fontsize=10)
axs[0].set_ylabel('L2 error', fontsize=9)
axs[0].set_xscale('log') 
axs[0].set_yscale('log') 
axs[0].plot(h2, L2Norm2, marker='o') 
axs[0].grid(True, which="both", ls="--") 
slope_L2, intercept_L2 = np.polyfit(np.log(h2), np.log(L2Norm2), 1)
print(f"L2 Error Linear Regression (log-log scale): Slope = {slope_L2}, Intercept = {np.exp(intercept_L2)}")

# Natural BC error and h figure
axs[1].set_title('Natural BC error with element length h', fontsize=10)
axs[1].set_xlabel('Element length h', fontsize=9)
axs[1].set_ylabel('Natural BC error', fontsize=9)
axs[1].plot(h2, natural_bc_error, marker='o', color='red') 
axs[1].grid(True) 
slope_nbc, intercept_nbc = np.polyfit(h2, natural_bc_error, 1)
print(f"Natural BC Error Linear Regression: Slope = {slope_nbc}, Intercept = {intercept_nbc}")

plt.tight_layout() 
plt.show() 




# Linear regression 
print("The L2 error norms are ")


a, C = np.polyfit(np.log(h2),np.log(L2Norm2),1)
print("    Linear element    : ||e||_L2 = %e h^%g" %(np.e**C, a))


# Convert matplotlib figures into PGFPlots figures stored in a Tikz file, 
# which can be added into your LaTex source code by "\input{fe_plot.tex}"
import tikzplotlib
tikzplotlib.save("fe_convergence.tex")


# Print error norms obtained by the linear element
#    with different element size
print("\nError norms of linear elements")
print('%13s %13s %13s' %('h','L2Norm','NaturalBC'))
for i in range(len(h2)):
    print('%13.6E %13.6E %13.6E' %(h2[i], L2Norm2[i], natural_bc_error[i]))

