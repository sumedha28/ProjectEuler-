#!/bin/python3

import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def get_number(n):
    ans = 1
    lst = [i for i in range(2, n+1)]
    for num in lst:
        ans = (ans*num) // gcd(ans, num)
        
    return ans
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = get_number(n)
    print(ans)
