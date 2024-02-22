# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
def get_sum_of_divisors(x):
    div_sum = 1
    for i in range(2, int(sqrt(x))+1):
        if x % i==0:
            div_sum+=i
            j = x//i
            if j!=i:
                div_sum += j
    return div_sum

def is_abdundant(x):
    if get_sum_of_divisors(x)>x:
        return True
    else:
        return False
            
t = int(input().strip())
n_values = [int(input().strip()) for _ in range(t)]
if max(n_values)>28123:
    n_max = 28124
else:
    n_max = max(n_values)+1

arr = []
for i in range(2, n_max):
    if is_abdundant(i):
        arr.append(i)

for n in n_values:
    flag = False
    if n>28123:
        flag = True
    elif n<12:
        flag = False
    else:
        for i in arr:
            x = n - i
            if x in arr:
                flag = True
                break
    if flag == True:
        print("YES")
    else:
        print("NO")
