#!/usr/bin/python

# reduzierte menge (restklasse modulo n)

from fractions import gcd

n = 216

L = []

for i in range(1,n):
	if(gcd(i,n)==1):
		L.append(i)

print(L)
