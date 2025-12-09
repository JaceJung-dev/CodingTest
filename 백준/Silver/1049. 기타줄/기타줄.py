import sys

input = sys.stdin.readline


N, M = map(int, input().split())

min_pack = float("inf")
min_sep = float("inf")
for _ in range(M):
    pack, sep = map(int, input().split())
    min_pack = min(min_pack, pack)
    min_sep = min(min_sep, sep)

case1 = N * min_sep
case2 = (N // 6) * min_pack + (N % 6) * min_sep
case3 = ((N + 5) // 6) * min_pack

print(min(case1, case2, case3))
