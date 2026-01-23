import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

non_prime = {0, 1, 4, 6, 8, 9}

answer = None
is_ok = False
for num in nums:
    if num in non_prime:
        is_ok = True
        answer = num

if is_ok:
    print("YES")
    print(answer)
else:
    prime = nums[0]
    print("YES")
    print(f"{prime}{prime}")

