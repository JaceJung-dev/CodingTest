import sys
input = sys.stdin.readline

N = int(input())
words = list({input().rstrip() for _ in range(N)})
words.sort()
print("\n".join(sorted(words, key=len)))