#!/bin/python3

import sys
from math import sqrt
            

primes = [True]*(10**6+1)

for i in range(2, int(sqrt(10**6))+1):
    for j in range(i*i, 10**6+1, i):
        primes[j] = False
        

sums = dict()
s = 0
for i in range(2, 10**6+1):
    if primes[i]:
        s += i
        sums[i] = s


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while n>1:
        if n in sums:
            print(sums[n])
            break
        n-=1
