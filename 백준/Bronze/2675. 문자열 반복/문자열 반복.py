T = int(input())
for _ in range(T):
    answer = ""
    R, S = input().split()
    for char in S:
        answer += char * int(R)
    print(answer)