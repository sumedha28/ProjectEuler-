# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.set_int_max_str_digits(0)
series = []
count_digits = dict()
a = 1
b = 1
count_digits[1] = 1
series.append(0)
series.append(a)
series.append(b)
i = 3
while True:
    c = a + b
    series.append(c)
    a = b
    b = c
    digits = len(str(c))
    if digits not in count_digits:
        count_digits[digits] = i
    i += 1
    if digits==5000:
        break
    
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(count_digits[n])
    
