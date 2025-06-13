N = int(input())

for _ in range(N):
    a, b = map(float, input().split())
    abs_distance = a - b
    if abs_distance < 0:
        abs_distance *= -1
    
    print(round(abs_distance, 1))