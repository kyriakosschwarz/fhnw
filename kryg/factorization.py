#!/usr/bin/python

# primfaktorzerlegung

# source: http://stackoverflow.com/questions/16996217/prime-factorization-list

n = 105

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
    
print primes(n)
