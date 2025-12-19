import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if even >= odd:
    print(2, 0)
else:
    print(2, 1)
