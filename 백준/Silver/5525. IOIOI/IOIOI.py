import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

count = 0
answer = 0
i = 0

while i <= M -3:
    if S[i] == "I" and S[i + 1] == "O" and S[i + 2] == "I":
        count += 1
    
        if count >= N:
            answer += 1
            count -= 1

        i += 2
    else:
        count = 0
        i += 1

print(answer)

