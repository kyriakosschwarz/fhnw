#!/usr/bin/python

# solution to euler 182
# https://projecteuler.net/problem=182

from fractions import gcd

p = 1009

q = 3643

n = p * q

fin = (p-1)*(q-1)

# possible e's
poses = [elem for elem in range(3,fin) if gcd(fin, elem) == 1]  

min = n

sum = 0

for e in poses:
	x = (1+gcd(e-1,p-1))*(1+gcd(e-1,q-1))
	if x < min:
		min = x

for e in poses:
	x = (1+gcd(e-1,p-1))*(1+gcd(e-1,q-1))
	if x == min:
		sum += e
		
print sum
