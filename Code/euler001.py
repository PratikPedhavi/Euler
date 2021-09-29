# Project Euler 1: sum of Multiples of 3 and 5 less than N
# Dated: 25092021
import sys

def sum_AP(n,d):
    # number of terms to be added in a series
    n = n//d
    n = int(n)
    out = n*(n+1)*d
    return int(out//2)

def sum_multiple(n):
    # all values less than n
    n -= 1
    return int(sum_AP(n,3) + sum_AP(n,5) - sum_AP(n,15))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_multiple(n))
