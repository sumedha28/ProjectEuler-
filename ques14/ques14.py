# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input().strip())
n = []
for i in range(t):
    n.append(int(input().strip()))
m = max(n)
answer = [1 for _ in range(m+1)]
result = [1 for _ in range(m+1)]

for i in range(2, m+1):
    count = 0
    curr = i
    while True:
        if curr<i:
            answer[i] = count + answer[curr]
            break
        if curr % 2 == 0:
            count += 1
            curr = curr//2
        else:
            count += 2
            curr = (3*curr + 1)//2

curr_max = 1
curr_ind = 1
for i in range(2, m+1):
    if answer[i] >= curr_max:
        curr_max = answer[i]
        curr_ind = i
    result[i] = curr_ind
    
for i in n:
    print(result[i])
