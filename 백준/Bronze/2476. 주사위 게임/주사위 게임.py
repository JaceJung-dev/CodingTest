import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
highest_prize = 0

for _ in range(N):
    dices = list(map(int, input().split()))
    count = Counter(dices)

    if 3 in count.values():
        dice = [k for k, v in count.items() if v == 3][0]
        prize = 10000 + dice * 1000
    elif 2 in count.values():
        dice = [k for k, v in count.items() if v == 2][0]
        prize = 1000 + dice * 100
    else:
        prize = max(dices) * 100

    highest_prize = max(highest_prize, prize)

print(highest_prize)
