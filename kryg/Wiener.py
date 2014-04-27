#!/usr/bin/python

# Kettenbruchentwicklung

import math
from fractions import *

e = 773
n = 2021

a = Fraction(e,n)

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

#print XI

####################################################################

L = list(XI)


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

#print K

#printfractfloat(K)

####################################################################

FI = []

for i in range(len(K)):
	#print 'e: ',e
	#print 'deltai: ', K[i].denominator
	#print 'kai: ', K[i].numerator
	if (K[i].numerator == 0) or ((((e*K[i].denominator)-1) % (K[i].numerator)) != 0) or ((((e*K[i].denominator)-1)/K[i].numerator) > n) :
		FI.append(0)
	else:
		FI.append(((e*K[i].denominator)-1)/K[i].numerator)
	
print FI

###################################################################

def findpq(n, fin):
	
	power = int(math.pow(n - fin + 1, 2))

	squareroot = int(math.sqrt(power - (4*n)))

	p = (n - fin + 1 + squareroot)/2

	q = n/p

	print '-----------p: ' , p

	print '-----------q: ' , q

i =1
for k in FI:
	print 'i: ', i
	if k != 0:
		findpq(n, k)
	i +=1

