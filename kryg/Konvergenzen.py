#!/usr/bin/python

# das umgekehrte der KE

import math
from fractions import *

#L = [5,3,2,1,4]
L = [0, 2, 1, 1, 1, 1, 2, 6, 4, 2]


def getres(L):
	if(len(L) == 1):
		return Fraction(L.pop(0), 1)
	else:
		return Fraction(L.pop(0), 1) + Fraction(1, getres(L))
		
def printfractfloat(L):
	for i in L:
		num = i.numerator
		den = i.denominator
		print num,'/',den,' = ', num/float(den), ", "

K = []

for i in range(len(L)):
	tmp = list(L)
	nextk = getres(L)
	K = [nextk] + K
	tmp.pop()
	L = list(tmp)

print K

printfractfloat(K)
