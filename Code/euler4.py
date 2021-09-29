# Project Euler 3: Largest Palindrome product of two 3-digit integers
# Dated: 2021-09-26

import sys

def get_the_palindrome1(N):
    greatPal = 0
    for i in range(999,100,-1):
        if greatPal > i*999:
            break
        for j in range(i,100,-1):
            greatInt = i*j
            if str(greatInt) ==str(greatInt)[::-1]:
                if greatInt < N and greatInt > greatPal:
                    greatPal = greatInt
                    print("i: {0} & j: {1}".format(i,j))
    return greatPal

def get_the_palindrome(N):
    palindromes = []
    for x in range(101,1000):
        # For this case particuarly the palindromes are Multiples of 11,
        # so the conditional increment is added in the For loop
        for i in range(121,1000,(1 if x%11==0 else 11)):
            num = str(i*x).split()[0]
            if int(num) < N:
                # element wise comparison is faster than str inversion comparison
                # of all elements
                if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
                    palindromes.append(i * x)
    return max(palindromes)


# t = int(input().strip())
t = 1
for a0 in range(t):
    n = int(input().strip())
    print(get_the_palindrome(n))
    print(get_the_palindrome1(n))
