# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_fact_sum(n):
    product = 1
    for i in range(n, 1, -1):
        product *= i
    return sum(list(map(int, str(product))))
    
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    ans = get_fact_sum(n)
    print(ans)
