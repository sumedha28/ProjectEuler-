#!/bin/python3

import sys
from math import sqrt

m = 110000
primes = [True]*(m+1)
primes[0] = primes[1] = False
for i in range(2, int(sqrt(m))+1):
    if primes[i]:
        for j in range(i*i, m+1, i):
            primes[j] = False
primes[2] = True
prime_th = [i for i in range(m+1) if primes[i]==True]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(prime_th[n-1])
    
