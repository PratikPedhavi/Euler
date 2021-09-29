# Project Euler 3: Largest prime factor
# Dated: 2021-09-26

import sys
import math

def prime_loop(n,divisor,maxPrime):
    while n%divisor == 0:
        maxPrime = divisor
        n //= divisor
    return n,maxPrime

def find_prime_factor(n):
    original = n
    maxPrime = n
    n,maxPrime = prime_loop(n,2,maxPrime)
    for divisor in range(3,int(math.sqrt(original))+1,2):
        n,maxPrime = prime_loop(n,divisor,maxPrime)
        n,maxPrime = prime_loop(n,divisor+2,maxPrime)
    return n if n>2 else maxPrime

# t = int(input().strip())
t = 1
for a0 in range(t):
    n = int(input().strip())
    print(find_prime_factor(n))
