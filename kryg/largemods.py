#!/usr/bin/python

# a^b mod m loesen

a = 61	
b = 5
m = 91

binb = bin(b)

#print binb

size = len(binb) -3

#print size

L = [int(i) for i in str(bin(b))[2:]]

print L

x = a % m

N = [x]

for j in range(size):
	pow2 = pow(x,2)
	x = pow2 % m
	N = [x] + N

print N

#print len(N)

product = 1

for k in range(size+1):
	#print 'k: ' , k
	#print 'product: ' ,product
	#print 'L[k]: ' ,L[k]
	#print 'N[k]: ' ,N[k]
	
	if(L[k]==1):
		product = product * N[k]
		
result = product % m
print 'res: ' ,result
