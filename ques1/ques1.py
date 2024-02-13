#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    mul_3_end = (n-1)//3
    mul_5_end = (n-1)//5
    mul_15_end = (n-1)//15
    mul_3 = 3*mul_3_end*(mul_3_end+1)//2
    mul_5 = 5*mul_5_end*(mul_5_end+1)//2
    mul_15 = 15*mul_15_end*(mul_15_end+1)//2
    total = mul_3 + mul_5 - mul_15
    print(total)
