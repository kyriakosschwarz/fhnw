#!/usr/bin/python

# das umgekehrte der KE

import math
from fractions import *

L = [5,3,2,1,4]

res  = Fraction(L.pop(0),1)

def getres(res, L):
	if(len(L) == 1):
		return Fraction(1, L.pop(0))
	else:
		item = L.pop(0)
		minifrac = Fraction(item,1)
		if(len(L) == 1):
			return res + Fraction(1, item + getres(minifrac, L))
		else:
			return res + Fraction(1, getres(minifrac, L))
		
res = getres(res,L)

print res	
