# Project Euler 9: Special pythagorean triplet
# Dated: 2021-10-13

import sys

def pythagorean_triplet(n):
    product = -1
    for k in range(int(n/4),n):
        j = int((n**2 - 2*n*k)/(2*n-2*k))
        i = int(n-k-j)
        if i <= 0 or j <=0:
            break
        if i**2 == k**2 + j**2:
            temp = i*j*k
            if product < temp and temp != 0:
                product = temp
    return product
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(pythagorean_triplet(n))
