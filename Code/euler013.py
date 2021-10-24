# Project Euler 13: Large sum for N 50-digit numbers
# Dated: 2021-10-24

import sys
from pdb import set_trace

'''
    Following problem is easier for python because python does not have
    limit on length of an integer
    sum50 function is irrelavant for Python
'''

# def sum50(A,N):
#     maxA = len(A)
#     maxN = len(N)
#     print(maxA,maxN)
#     for k in range(maxN):
#         carry = (int(A[k]) + int(N[maxN-k-1]))//10
#         A[k+1] = str(int(A[k+1]) + carry)
#         A[k] = str((int(A[k]) + int(N[maxN-k-1]))%10)
#     return A
#
# A = ['0']*60
# t = int(input().strip())
# for _ in range(t):
#     n = str(input().strip())
#     A = sum50(A,n)
#     print(A)
#
# count = len(A)
# for k in range(len(A)-1,0,-1):
#     if A[k] == '0':
#         count = k
#     else:
#         break
# B = A[:count]
# B = B[::-1]
# print(count,B)
# print(int(''.join(B[:10])))


total50 = 0
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    total50 += int(n)
print(int(str(total50)[:10]))
