#!/usr/bin/env python3

import FEData as model
from utitls import gauss
import numpy as np


def Tri2DElem(e):
	"""
	Calculate element stiffness matrix and element nodal body force vector

	Args:
		e : (int) element number

	Returns: ke, fe
		ke : (numpy(nen,nen)) element stiffness matrix
		fe : (numpy(nen,1)) element nodal force vector
	"""
	ke = np.zeros((model.nen*model.ndof, model.nen*model.ndof))
	fe = np.zeros((model.nen*model.ndof, 1))

	# get coordinates of element nodes
	je = model.IEN[:, e] - 1
	C = np.array([model.x[je], model.y[je]]).T
	a, b, c, Ae=ParamCalc(C)
  
	# derivative of shape function
	B = BmatTri2D(C)
	ke = Ae * B.T @ model.D @ B
	
	# compute element nodal force vector
	fe = Ae * model.b[:, e].reshape((-1, 1))
	fe = fe / 3
	
	return ke, fe


def NmatTri2D(x, y, C):
	"""
	Calculate element shape function matrix N at coordinate xt

	Args:
		Ae: Area of the element in physical coordinates
		

	Returns:
		Element shape function matrix N
	"""
	a, b, c, Ae = ParamCalc(C)

	N1 = (a[0] + b[0] * x + c[0] * y) / (2 * Ae)
	N2 = (a[1] + b[1] * x + c[1] * y) / (2 * Ae)
	N3 = (a[2] + b[2] * x + c[2] * y) / (2 * Ae)

	return np.array([[N1, 0, N2, 0, N3, 0],
					 [0, N1, 0, N2, 0, N3]])


def BmatTri2D(C):
	"""
	Calcualte derivative of element shape function matrix B at coordinate xt

	Args:
		C   : The physical coordinates

	Returns:
		Derivative of element shape function matrix B and Jacobian determination
	"""
	a, b, c, Ae = ParamCalc(C)
	
	B = np.array([[b[0], 0, b[1], 0, b[2], 0],
				  [0, c[0], 0, c[1], 0, c[2]],
				  [c[0], b[0], c[1], b[1], c[2], b[2]]]) / (2*Ae)
	

	return B



def ParamCalc(C):
	'''
	Calculate a b and c in Shape function N and B

	Args:
		C: coordinate vetor of the element in physical coordnates
	'''
	a = np.zeros(3)
	b = np.zeros(3)
	c = np.zeros(3)
	
	a[0]=C[1][0]*C[2][1]-C[2][0]*C[1][1]
	a[1]=C[2][0]*C[0][1]-C[0][0]*C[2][1]
	a[2]=C[0][0]*C[1][1]-C[1][0]*C[0][1]

	b[0]=C[1][1]-C[2][1]
	b[1]=C[2][1]-C[0][1]
	b[2]=C[0][1]-C[1][1]

	c[0]=C[2][0]-C[1][0]
	c[1]=C[0][0]-C[2][0]
	c[2]=C[1][0]-C[0][0]
	
	Ae=0.5 * np.sum(a)
	

	return a, b, c, Ae

