#!/usr/bin/python

# 

import math

p = 2099

q = 1699  # p > q

def enth_root(val, n):
    ret = val**(1./n)
    return ret + 1 if (ret + 1) ** n == val else ret

n = p * q

print 'n: ', n

delta = p - q

print 'delta: ' , delta

c = 1

sq4 = enth_root(n, 4)

print 'sq4: ', sq4

cond = delta < c * sq4

print 'cond: ', cond 

while(not cond):
	c += 1
	print 'c: ' , c
	cond = delta < c * sq4
	
#res = int(math.floor(math.sqrt(c)/8))

res = int(math.floor(math.pow(c,2)/float(8)))

if res == 0:
	res = 1

print 'res: ' , res
