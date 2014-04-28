#!/usr/bin/python

# SAGE

e1 = 3
e2 = 7
n = 53687553757

c1 = 52276469171
c2 = 27288083842

tup = xgcd(e1, e2)

a = tup[1]
b = tup[2]

m = (c1.powermod(a,n) * c2.powermod(b, n)) % n

print m
