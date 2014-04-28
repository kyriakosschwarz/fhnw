#!/usr/bin/python

# 

import math

s = 9

t = 22

a = t+s

b = t-s

print a,b

#n = a * b

n = 11209459057

def issquare(n):
	x = int(math.floor(math.sqrt(n)))
	return int(math.pow(x,2)) == n
	
te = math.floor(math.sqrt(n)) +1
print 'te0: ', te

cond = math.pow(te,2) - n

print 't^2 - n0: ',cond

while (not issquare(cond)):
	print 'te: ',te
	te += 1
	cond = math.pow(te,2) - n
	print 't^2 - n:', cond


se = math.sqrt(cond)
print 'se: ' , se

alpha = te + se

beta = te - se

print alpha, beta


