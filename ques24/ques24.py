# Enter your code here. Read input from STDIN. Print output to STDOUT 
from itertools import permutations

def get_nth_perm(n, strng):
    s = []
    result = ""
    strng = list(strng)
    n = n-1
    for i in range(1, len(strng)+1):
        s.append(n%i)
        n = n//i
    
    for i in range(len(strng)):
        a = s[-1]
        result += strng[a]
        
        for j in range(a, len(strng)-1):
            strng[j] = strng[j+1]
        strng[j+1] = '\0'
        s.pop()
        
    return result

strng = 'abcdefghijklm'
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    res = get_nth_perm(n, strng)
    print(res)
