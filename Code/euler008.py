# Project Euler 8: Largest product in a series
# Dated: 2021-10-13

import sys

def largest_product(n,k,num):
    num_list = [int(k) for k in str(num)]
    greatest = 0
    for i in range(0,n+1-k):
        new = get_products(num_list[i:i+k])
        if new > greatest:
            greatest = new
    return greatest

def get_products(num_sub):
    new = 1
    for j in num_sub:
        new *= j
    return new

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(largest_product(n,k,num))
