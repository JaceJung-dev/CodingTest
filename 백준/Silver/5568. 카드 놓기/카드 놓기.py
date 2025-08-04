import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
              
cards = [input().strip() for _ in range(n)]

result = set()

def pick(temp, used):
    if len(temp) == k:
        num = "".join(temp)
        result.add(num)
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            pick(temp + [cards[i]], used)
            used[i] = False
            
used = [False] * n
pick([], used)

print(len(result))