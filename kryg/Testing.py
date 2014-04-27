#!/usr/bin/python

# das umgekehrte der KE

import math
from fractions import *

L = [5,3,2,1,4]



def getres(L):
	if(len(L) == 1):
		return Fraction(L.pop(0), 1)
	else:
		return Fraction(L.pop(0), 1) + Fraction(1, getres(L))
		
res = getres(L)

print res	
