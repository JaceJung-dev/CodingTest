N = int(input())

for _ in range(N):
    a, b = map(float, input().split())
    abs_distance = abs(a - b)
    
    print(round(abs_distance, 1))