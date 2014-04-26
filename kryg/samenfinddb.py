#!/usr/bin/python

# wenn Alice und Bob das gleiche n haben
# bekannt: (n, ea) (n, da)
#		   (n, eb) (n, ??)
# zu finden: db

from fractions import gcd

n = 91
ea = 7
da = 31
eb = 5

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

mult = (ea * da) -1

print mult

gc = gcd(mult, eb)

print gc

h = mult/gc	

print 'h: ' ,h

d = gcd(eb, h)

print d

while(d != 1):
	h = h/d
	d = gcd(eb, h)
	
print 'endwhile'

a = exteucl(eb, h)

print 'a: ' , a

dbsch = a % h

print 'dbsch: ' ,dbsch
