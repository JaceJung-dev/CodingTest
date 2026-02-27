import sys

input = sys.stdin.readline

N = int(input())
word = input().strip()

for i in range(1, N):
    prefix = word[0:i]
    suffix = word[N - i : N]

    diff_count = 0
    for j in range(i):
        if prefix[j] != suffix[j]:
            diff_count += 1
        if diff_count > 1:
            break

    if diff_count == 1:
        print("YES")
        break
else:
    print("NO")