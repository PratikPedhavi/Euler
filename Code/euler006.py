# Project Euler 6: Sum square difference
# Dated: 2021-09-29

import sys
import math

def square_sum(N):
    return sum(range(N+1))**2

def sum_square(N):
    return N*(N + 1)*(2*N + 1)/6

def abs_diff(N):
    return int(abs(square_sum(N)-sum_square(N)))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(abs_diff(n))
