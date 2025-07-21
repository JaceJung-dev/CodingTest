import sys
input = sys.stdin.readline

N = input().strip()
length = len(N)
count = 0

for i in range(1,length):
    count += 9 * (10 ** (i - 1)) * i
count += (int(N) - 10 ** (length - 1) + 1) * length

print(count)