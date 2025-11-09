import sys

input = sys.stdin.readline

N = int(input())
candy = list(map(int, input().split()))

start = 0
max_len = 0
candy_count = {}

for end in range(N):
    candy_count[candy[end]] = candy_count.get(candy[end], 0) + 1

    while len(candy_count) > 2:
        candy_count[candy[start]] -= 1
        if candy_count[candy[start]] == 0:
            del candy_count[candy[start]]
        start += 1
        
    max_len = max(max_len, end - start + 1)

print(max_len)