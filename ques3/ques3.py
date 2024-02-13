#!/bin/python3

import sys
from math import sqrt
def is_prime(i):
    for a in range(2, int(sqrt(i))+1):
        if i % a == 0:
            return False
    return True

def find_prime(n):
    ans = -1
    for x in range(int(sqrt(n)), 1, -1):
        #print("x", x)
        if n % x == 0:
            ans1 = -1
            ans2 = -1
            #print("True")
            if is_prime(x):
                ans1 = x
                #print("ans1", ans1)
            if is_prime(n/x):
                ans2 = n//x
                #print("ans2", ans2)
            if ans1!=-1 and ans2!=-1:
                if ans1>ans2:
                    ans = ans1
                else:
                    ans = ans2
                break
            if ans1!=-1 and ans2==-1:
                ans = ans1
                break
            if ans2!=-1 and ans1==-1:
                ans = ans2
                break
            
    if ans==-1:
        return n
    else:
        return ans

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = find_prime(n)
    print(ans)
