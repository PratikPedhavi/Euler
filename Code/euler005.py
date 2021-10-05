# Project Euler 5: Smallest multiple
# Dated: 2021-09-29

import sys
import math

def smallest_multiple(N):
    if N > 0:
        return int((N*smallest_multiple(N-1))/math.gcd(N,smallest_multiple(N-1)))
    else:
        return 1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))
