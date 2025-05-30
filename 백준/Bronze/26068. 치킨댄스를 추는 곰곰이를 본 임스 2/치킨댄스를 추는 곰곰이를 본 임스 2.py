N = int(input())
count = 0

for _ in range(N):
    deadline = input()
    day_left = int(deadline[2:])
    if day_left <= 90:
        count += 1
print(count)
    