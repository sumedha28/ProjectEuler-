# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
names = []
for i in range(n):
    names.append(input().strip())
scores = dict()
for name in names:
    curr_name = name
    name = list(name)
    score = 0
    for i in range(len(name)):
        #print(name[i], " ", ord(name[i]))
        score += (ord(name[i])-64)
    scores[curr_name] = score
scores = dict(sorted(scores.items()))
i = 1
for k in scores.keys():
    scores[k] = i*scores[k]
    i += 1 
q = int(input().strip())
for i in range(q):
    word = input().strip()
    if word in scores:
        print(scores[word])
    else:
        print("NA")
