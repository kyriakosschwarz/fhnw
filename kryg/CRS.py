#!/usr/bin/python

# chinesischer restsatz

MI = [14803,26989,49087]

AI = [7355,5085,12613]

e = 3

size = len(MI)

def enth_root(val, n):
    ret = int(val**(1./n))
    return ret + 1 if (ret + 1) ** n == val else ret

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

m = 1

for mi in MI:
	m *= mi
	
print 'm: ' , m

M = []

i =1
for mi in MI:
	M.append(m/mi)
	i += 1
	
print 'M: ' , M

YI = []


for k in range(size):
	YI.append(exteucl(M[k],MI[k]))

print 'YI: ' , YI

sum=0
for k in range(size):
	#print 'AI[k]:' , AI[k] 
	#print 'YI[k]:' , YI[k]
	#print 'M[k]:' , M[k]
	sum += (AI[k] * YI[k] * M[k])
	
print sum
	
x = sum % m

print 'x: ' , x

m = enth_root(x,e)

print 'm: ' , m
