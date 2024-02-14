#!/bin/python3

import sys

    
def get_palindrome(n):
    ans = -1
    
    for i in range(999, 99, -1):
        for j in range(999, 99, (-1 if i % 11 == 0 else -11)):
            curr = i*j
            if curr<n and curr>=101101:
                if (str(curr)==str(curr)[::-1]):
                    ans = max(curr, ans)
                   
    return ans

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = get_palindrome(n)
    print(ans)
