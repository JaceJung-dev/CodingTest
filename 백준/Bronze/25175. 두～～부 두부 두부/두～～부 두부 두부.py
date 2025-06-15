# 1. 전체 인원, 현재 기준점 M, 이동하는 값 K
# 2. 순환형이니까 모듈러 생각해보기

N, M, K = map(int, input().split())
next_person = (M + K - 3) % N
if next_person == 0:
    print(N)
else:
    print(next_person)