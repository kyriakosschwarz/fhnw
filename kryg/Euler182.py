#!/usr/bin/python

# solution to euler 182
# https://projecteuler.net/problem=182

from fractions import gcd

p = 1009
q = 3643
fin = (p-1)*(q-1)
min = 9
sum = 0

for e in range(3, fin):
	if ( gcd(fin, e) == 1 ) and ( (1+gcd(e-1,p-1)) * (1+gcd(e-1,q-1)) == min ):
		sum += e
		
print sum
