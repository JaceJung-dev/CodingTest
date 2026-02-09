import sys

input = sys.stdin.readline

alphabet = set("abcdefghijklmnopqrstuvwxyz")

N = int(input())
for _ in range(N):
    sentence = input().strip().lower()

    contained = set(char for char in sentence if ord("a") <= ord(char) <= ord("z"))

    left = sorted(alphabet - contained)

    if left:
        print(f"missing {''.join(left)}")
    else:
        print("pangram")
