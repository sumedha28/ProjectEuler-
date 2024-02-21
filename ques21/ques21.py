# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
def get_proper_divisors_sum(x):
    proper_divisors = [1]
    
    for i in range(2, 1 + int(sqrt(x))):
        if x % i == 0:
            proper_divisors.append(i)
            j = x//i
            if j!=i:
                proper_divisors.append(j)
            
    return sum(proper_divisors)

t = int(input().strip())
n_values = [int(input().strip()) for _ in range(t)]

pairs = set()
d_values = dict()
#d_values[1] = 1

for i in range(2, 10**5+50000):
    curr = get_proper_divisors_sum(i)
    #print("Proper divisors sum of i: ", i, " is: ", curr)
    d_values[i] = curr
    if curr in d_values.keys() and d_values[curr]==i:
        #print("Pair found", curr, d_values[i])
        if i!=curr:
            pairs.add((i, curr))


#print(pairs)
for n in n_values:
    final_sum = 0
    for x, y in pairs:
        if x<=n or y<=n:
            #print("Pairs under n: ", n, " are : ", x, " and ", y)
            if x<=n:
                final_sum += x
            if y<=n:
                final_sum += y
    print(final_sum)
