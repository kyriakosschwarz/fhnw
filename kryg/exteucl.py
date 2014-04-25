#!/usr/bin/python

# extended euclidian algorithm

e = 5
fin = 1959888 # fi von n
 
x = e
y = fin

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

print '(e*d + k*fin)==1 : ' , (e*d + k*fin)==1
