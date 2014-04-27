#!/usr/bin/python

# Kettenbruchentwicklung

import math
from fractions import *

a = Fraction(37,7)

def getxi(a):
	num = a.numerator
	den = a.denominator
	alpha = num / float(den)
	xi = int(math.floor(alpha))
	return xi

KSI = [a]

XI = [getxi(a)]

i = 0

while((KSI[i] - XI[i]) != 0):
	nextksi = 1/(KSI[i] - XI[i])
	KSI.append(nextksi)
	XI.append(getxi(nextksi))
	i += 1

print XI

