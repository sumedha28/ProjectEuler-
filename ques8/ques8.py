import sys

def get_result(num, k, n):
    max_prod = -1
    for i in range(0, n-k):
        lst = list(map(int, str(num)[i:i+k]))
        #print("List: ", lst)
        curr = 1
        #print("i: ", i)
        for el in lst:
            #print(el)
            curr = curr*el
            #print("curr prod: ", curr)
        max_prod = max(max_prod, curr)
    return max_prod

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    ans = get_result(num, k, n)
    print(ans)
