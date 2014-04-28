#!/usr/bin/python

# 

import math

p = 667181 

q = 815333

n = p * q

e = 18439769619

def exteucl(eb, h): # extended euclidian algorithm
	x = eb
	y = h

	q = 0
	r = 0

	u = 1
	uton = 0

	v = 0
	vton = 1

	sign = 1

	while(y != 0):
		q = x/y
		r = x%y
		
		x = y
		y = r
		
		tempu = q*u + uton
		uton = u
		u = tempu
		
		tempv = q*v + vton
		vton = v
		v = tempv
		
		sign = sign * (-1)	

	d = sign * vton
	print 'd: ', d
	k = sign * (-1) * uton
	print 'k: ' ,k
	print '(e*d + k*fin)==1 : ' , (eb*d + k*h)==1
	return d
	
