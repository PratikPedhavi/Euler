# Project Euler 7: 10001st prime
# Dated: 2021-10-06

import sys

def sieveOfEratosthenes():
    n = 1000005
    primes = {}
    prime = [True for i in range(n+1)]
    p = 2
    while p*p < n:
        if prime[p]:
            for k in range(p*p,n+1,p):
                prime[k]=False

        p+=1
    i=1
    for p in range(2,n+1):
        if prime[p]:
            primes[i] = p
            i += 1
    return primes

t = int(input().strip())
primes = sieveOfEratosthenes()
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])
