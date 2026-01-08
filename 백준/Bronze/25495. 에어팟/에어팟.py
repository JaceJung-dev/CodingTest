import sys

input = sys.stdin.readline

N = int(input())
phones = list(map(int, input().split(" ")))

total_consumption = 0
consumption = 0
prev = None

for phone in phones:
    if phone == prev:
        consumption *= 2
    else:
        consumption = 2

    total_consumption += consumption
    prev = phone

    if total_consumption >= 100:
        total_consumption = 0
        prev = None

print(total_consumption)
