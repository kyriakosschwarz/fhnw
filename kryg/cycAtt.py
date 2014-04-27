#!/usr/bin/python

# SAGE

def cycAtt(c,e,n):
    a = c.powermod(e,n)
    i = 1
    while a != c :
        b = a
        a = a.powermod(e,n)
        i = i + 1
    return [b,i]

p = 47
q = 23
n = p*q

m = 666

e = 3
c = m.powermod(e,n)
print 'c: ' ,c

cycAtt(c,e,n)
