# Project Euler 2: Even Fibonacci
# Dated: 26092021
import sys

def fibonacci(n):
    prev_num = 0
    next_num = 1
    even_sum = 0
    while next_num < n:
        if next_num%2 == 0:
            even_sum += next_num
        temp = next_num
        next_num = next_num + prev_num
        prev_num = temp
        # print(next_num)
    return even_sum

def fast_even(n):
    prev_num = 0
    next_num = 2
    even_sum = 0
    while next_num<n:
        even_sum += next_num
        temp = next_num
        next_num = next_num*4+prev_num
        prev_num = temp
    return even_sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print("Even Sum: ", fibonacci(n))
    print("Fast Even Sum: ", fast_even(n))
