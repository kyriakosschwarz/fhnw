#!/usr/bin/python

# SAGE

e1 = 3
e2 = 11
n = 187

c1 = 65
c2 = 54

tup = xgcd(e1, e2)

a = tup[1]
b = tup[2]

m = (c1.powermod(a,n) * c2.powermod(b, n)) % n

print m
