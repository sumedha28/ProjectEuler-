# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    num = 2**n
    print(sum(list(map(int, str(num)))))
