# Project Euler 10: Summation of primes
# Dated: 2021-10-14

import sys

def prime_set():
    n = 1000001
    primes = [True]*n
    primes_sum = [0]*n
    primes[0] = primes[1] = False
    for p,isPrime in enumerate(primes):
        if isPrime:
            primes_sum[p] = primes_sum[p-1] + p
            for k in range(p*p,n,p):
                primes[k] = False
        else:
            primes_sum[p] = primes_sum[p-1]
    return primes_sum

t = int(input().strip())
set_pri = prime_set()
for a0 in range(t):
    n = int(input().strip())
    print(set_pri[n])
