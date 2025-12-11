import sys

input = sys.stdin.readline

N = int(input())

g_member = [1, 2, 3, 3, 4, 10]
s_member = [1, 2, 2, 2, 3, 5, 10]
for i in range(N):
    gandal = list(map(int, input().split()))
    sauron = list(map(int, input().split()))

    g_score = sum(g_member[j] * gandal[j] for j in range(len(gandal)))
    s_score = sum(s_member[j] * sauron[j] for j in range(len(sauron)))

    if g_score > s_score:
        print(f"Battle {i + 1}: Good triumphs over Evil")
    elif g_score < s_score:
        print(f"Battle {i + 1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i + 1}: No victor on this battle field")
