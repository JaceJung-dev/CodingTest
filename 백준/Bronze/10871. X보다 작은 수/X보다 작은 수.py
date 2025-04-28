N , X = map(int, input().split())
A = list(map(int, input().split()))
answer = []
for num in A:
    if num < X:
        answer.append(num)
print(*answer)