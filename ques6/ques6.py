#!/bin/python3

import sys

def get_sum_squared(x):
    return ((x*(x+1)//2))**2
    
def get_squared_sum(x):
    return (x*(x+1)*(2*x+1))//6

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_squared = get_sum_squared(n)
    squared_sum = get_squared_sum(n)
    print(abs(sum_squared - squared_sum))
