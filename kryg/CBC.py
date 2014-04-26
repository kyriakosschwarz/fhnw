#!/usr/bin/python

# format(b, '#06b')

m = 0b110001101100101

tmp = m

C0 = 0b1110

size = 0

while (tmp!=0):
	tmp = tmp >> 1
	#print tmp
	size += 1
	
print size

pad = 4 - (size % 4)

print pad

if(pad > 0):
	m = m << 1
	m += 1

if(pad > 1):
	m = m << 1

if(pad > 2):
	m = m << 1


print bin(m)

size = size +1

ms = size / 4

print ms


