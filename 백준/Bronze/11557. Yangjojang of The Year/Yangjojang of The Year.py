import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    max_school = ""
    max_amount = -1
    for _ in range(N):
        school, amount = input().split()
        if int(amount) > max_amount:
            max_amount = int(amount)
            max_school = school

    print(max_school)
