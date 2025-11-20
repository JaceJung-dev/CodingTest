import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num1 = input().strip()
    num2 = input().strip()

    dist = sum(char1 != char2 for char1, char2 in zip(num1, num2))
    print(f"Hamming distance is {dist}.")
