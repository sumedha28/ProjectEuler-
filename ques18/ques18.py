# Enter your code here. Read input from STDIN. Print output to STDOUT
max_sum = [0]

def get_max_total(traingle, lvl, i, lsum):
    m = i
    n = i+1
    if lvl==(len(traingle)-1):
        max_sum[0] = max(max_sum[0], lsum + traingle[lvl][m], lsum + traingle[lvl][n])
        return
    get_max_total(traingle, lvl+1, m, lsum + traingle[lvl][m])
    get_max_total(traingle, lvl+1, n, lsum + traingle[lvl][n])
    
    
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    traingle = []
    max_sum[0] = 0
    k = 0
    for j in range(n):
        curr = list(map(int, input().split()))
        traingle.append(curr)
        k += 1
    #print(traingle)
    #print(len(traingle))
    if n>1:
        get_max_total(traingle, 1, 0, traingle[0][0])
        
    print(max(max_sum[0], traingle[0][0]))
