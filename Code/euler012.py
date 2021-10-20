# Project Euler 12: Highly divisible triangular number
# Dated: 2021-10-20

import sys
import math

def get_divisors(N):
    divisors = [1]
    n = 2
    for k in range(n,int(math.sqrt(N))+1):
        if N%k == 0:
            divisors.extend([k,int(N/k)])
    divisors.extend([N])
    return set(divisors)

def generate_triangular():
    '''
    for every triangular number we are calculating
    its divisors from the numbers less than itself
    '''
    num = 1000
    triangle_list = [1]
    trian = 1
    trian_sum = 0
    count = 0
    for k in range(1,num+1):
        while count <= k:
            trian_sum = ((trian+1)*trian/2)
            divisors = get_divisors(trian_sum)
            count = len(divisors)
            trian += 1
        triangle_list.append(trian_sum)
    return trian_sum

def build_triangle(N, nMax = 45000):
    '''Concept of co-prime and their divisors is considered for this approach.'''
    d = [0]*nMax
    for i in range(1,nMax):
        for j in range(i,nMax,i):
            d[j] += 1
        nDiv = d[i-1]*d[i//2] if i%2 == 0 else d[(i-1)//2]*d[i]
        if nDiv > N: return i*(i-1)//2

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(build_triangle(n))
