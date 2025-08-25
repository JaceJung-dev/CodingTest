import sys
input = sys.stdin.readline

N = int(input())
words = list({input().rstrip() for _ in range(N)})

l = sorted(list({len(w) for w in words}))

res = []
for i in l:
    temp = []
    for word in words:
        if len(word) == i:
            temp.append(word)
    temp.sort()
    res += temp
    
for w in res:
    print(w)