# N을 줄여나가면서 반복
# 성충, 번데기, 유충 숫자를 계속 업데이트 해나가는 방식


while True:
    try:
        M, P, L, E, R, S, N = map(int, input().split())

        while N > 0:
            N -= 1
            C = P // S
            P = L // R
            L = M * E
            M = C
        print(C)
    
    except:
        break