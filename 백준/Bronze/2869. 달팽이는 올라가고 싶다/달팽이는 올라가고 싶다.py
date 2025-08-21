import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

print((V - B + (A - B) - 1) // (A - B))
