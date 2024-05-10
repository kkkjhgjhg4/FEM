#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot exact solutions for some problems
	ExactSolution_Cantilever: Plot the exact solution of the cantilever given
	in Example 10.1 in Fish's textbook

Created on Aug. 15 2022

@author: jsli@163.com, xzhang@tsinghua.edu.cn
"""

import numpy as np
import math 
import matplotlib.pyplot as plt
import FEData as model

from Elast2DElem import NmatElast2D, BmatElast2D
from utitls import gauss


def Exact(ax1):
	"""
	Plot the exact deflection and moment Mx along the centerline
	of the plate(Example 6-3) in ax1 and ax2, respectively.

	Args:
		ax1 : axis to draw deflection distribution
		ax2 : axis to draw moment Mx distribution
	"""
	a=1
	b=4
	pa=1
	pb=0
	E=13
	
	dx = 0.1
	nx  = math.ceil((b-a) / dx)
	x = np.arange(a, b, dx)
	sigma_rr = np.zeros(nx, np.float)

	for index, xi in enumerate(x):
		sigma_rr[index] = (pa*a**2-pb*b**2)/(b**2-a**2) - a**2*b**2/(b**2-a**2)/xi**2*(pa-pb)

	xplot = np.arange(a, b, dx)
	line5, = ax1.plot(xplot, sigma_rr, 'r', label='Exact')

def sigmarr():
	"""
	Plot deflection and moment Mx distributions along the radius
	
	"""
	nplot=21
	
	xplot = np.zeros(4*nplot)
	sigma_rr = np.zeros(4*nplot)
	
	xplot_osp = np.zeros(4)
	sigma_osp = np.zeros(4)
	
	e_all = np.array([7, 15, 23, 31])
	
	for index, e in enumerate(e_all):
		
		# get coordinate and deflection of element nodes
		je = model.IEN[:, e] - 1
		C = np.array([model.x[je], model.y[je]]).T
		de = model.d[model.LM[:,e]-1]
		
		# equally distributed coordinates on the psi = 1 line of an element
		
		xplot_e = np.linspace(C[1,0], C[2,0], nplot)
		etaplot = 0.0
		psiplot = (2*xplot_e - C[1,0] - C[2,0])/(C[2,0] - C[1,0])
		
		sigma_rr_e = np.zeros(nplot)
		sigma_all = np.zeros(3)
		n = np.array([0.980785280403230, 0.195090322016128])
		
		for i in range(nplot):
			psi = psiplot[i]
			B, detJ = BmatElast2D(etaplot, psi, C)
			sigma_all = model.D@B@de
			sigma_rr_e[i] = (sigma_all[0]+sigma_all[1])/2.0 + (sigma_all[0]-sigma_all[1])/2.0*n[0] - sigma_all[2]*n[1]
		
		xplot[index*nplot:(index+1)*nplot] = xplot_e[:]
		sigma_rr[index*nplot:(index+1)*nplot] = sigma_rr_e[:]
		
		xplot_osp[index] = xplot_e[10]
		sigma_osp[index] = sigma_rr_e[10]
		
	return xplot, sigma_rr, xplot_osp, sigma_osp

def exact_4_12(x,y):
	'''
		exact solution of exercise 4_12
	'''
	u = 0.048 * x * y
	v = -0.024 * np.power(x, 2)
	sxx = 480 * y

	return u, v, sxx * 0.0001



def ErrorNorm_4_12():
	""" 
	Calculate and print the error norm (L2 norm) of exercise 4.12

	Return the L2Norm Error and h
	"""
	
	ngp = 2
	w, gp = gauss(ngp)    # extract Gauss points and weights

	beam_height = 0.5       # geo pramras of the beam
	beam_length = 5

	L2Norm = 0

	EnergyNorm = 0


	# compute the L2 and Energy error norm element-wise
	for e in range(model.nel):
		# get coordinates of element nodes
		je = model.IEN[:, e] - 1
		C = np.array([model.x[je], model.y[je]]).T
		# extract element nodal displacements
		de = model.d[model.LM[:, e] - 1]		
		# compute the L2Norm = uex - uh gauss intergration
		# here we calculate the displacement field in parent space first then using Jacobian to transfer
		for i in range(ngp):
			for j in range(ngp):
				eta = gp[i]
				psi = gp[j]
				Be, detJe = BmatElast2D(eta, psi, C)
				Ne = NmatElast2D(eta, psi)

				# transfer parent coordinate to physical for exact displacement
				x_exact = 0.25*(1-psi)*(1-eta) * C[0][0] + 0.25*(1+psi)*(1-eta) * C[1][0] + 0.25*(1+psi)*(1+eta) * C[2][0] + 0.25*(1-psi)*(1+eta) * C[3][0]
				y_exact = 0.25*(1-psi)*(1-eta) * C[0][1] + 0.25*(1+psi)*(1-eta) * C[1][1] + 0.25*(1+psi)*(1+eta) * C[2][1] + 0.25*(1-psi)*(1+eta) * C[3][1]
				
				# for 2d problem, displacement field is a 2*1 vector
				u, v, sxx= exact_4_12(x_exact, y_exact)
				uh = Ne @ de # displacement in parent space
				error_x = uh[0] - u
				error_y = uh[1] - v
				Nabla_u = np.array([sxx, 0.0, 0.0])

				L2Norm +=  w[i] * w[j] * (np.power(error_x, 2) + np.power(error_y, 2)) * detJe
				EnergyNorm += w[i] * w[j] * (Nabla_u - Be @ de).T @ model.D @ (Nabla_u - Be @ de) * detJe

	# L2Norm is the sqrt of the integral
	L2Norm = np.sqrt(L2Norm)
	# EnergyNorm is 1/2 and sqrt of the a
	EnergyNorm = 0.5 * np.sqrt(EnergyNorm)

	# diagonal_length h
	N = np.sqrt(model.nel/5)
	h = np.sqrt((beam_height/N)**2 + (beam_length/N)**2)

	# print Error norms
	print('\nError norms')
	print('%13s %13s %13s '
		  %('h','L2Norm','EnergyNorm'))
	print('%13.6E %13.6E %13.6E\n'
		  %(h, L2Norm, EnergyNorm))
	
	return h, L2Norm, EnergyNorm