import sys
input = sys.stdin.readline

days = [0] * 5
N = int(input())
for _ in range(N):
    person_available_days = input()
    for i in range(len(person_available_days)):
        if person_available_days[i] == "Y":
            days[i] += 1

largest_num = max(days)
largest_days = [i + 1 for i, v in enumerate(days) if v == largest_num]

print(",".join(map(str, largest_days)))

    