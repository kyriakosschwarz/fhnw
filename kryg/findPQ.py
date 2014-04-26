#!/usr/bin/python

# finde p und q wenn man n und fi von n kennt

import math

n = 77075627

fin = 77057976

power = int(math.pow(n - fin + 1, 2))

squareroot = int(math.sqrt(power - (4*n)))

p = (n - fin + 1 + squareroot)/2

q = n/p

print 'p: ' , p

print 'q: ' , q
