#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = 1
    b = 2
    sum_f = 2
    for i in range(n-2, 0, -1):
        #print("Iteration number: ", i)
        c = a+b
        #print("Before changes: ", a, b, c)
        a = b
        b = c
        if c>n:
            break
        #print("After changes: ", a, b, c)
        if c % 2 == 0:
            sum_f += c
        #    print("Current sum: ", sum_f)
    print(sum_f)
    
