import sys
input = sys.stdin.readline

while True:
    M, A, B = map(int, input().split())
    
    if (M, A, B) == (0, 0, 0):
        break
        
    train_time = M / A * 3600
    plane_time = M / B * 3600
    
    gap = train_time - plane_time
    
    h = int(gap // 3600)
    m = str(int((gap % 3600) // 60)).zfill(2)
    s = str(round((gap % 3600) % 60)).zfill(2)
    print(f"{h}:{m}:{s}")    