import sys

input = sys.stdin.readline

count = 0


N, M = map(int, input().split())
unseen = {input().strip() for _ in range(N)}
unheard = {input().strip() for _ in range(M)}

intersection = sorted(list(unseen & unheard))

print(len(intersection))
print("\n".join(intersection))
