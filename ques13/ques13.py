# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input(). strip())
a = []
for i in range(0, n):
    a.append(int(input().strip()))

s = sum(a)
print(str(s)[:10])
