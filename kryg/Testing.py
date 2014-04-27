#!/usr/bin/python

# das umgekehrte der KE

import math
from fractions import *

def enth_root(val, n):
    ret = int(val**(1./n))
    return ret + 1 if (ret + 1) ** n == val else ret

x = math.pow(3, 4)

print enth_root(x,4)
