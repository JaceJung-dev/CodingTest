import sys
input = sys.stdin.readline

N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]
dots.sort(key=lambda x: (x[0], x[1]))

for dot in dots:
    print(dot[0], dot[1])
    

    