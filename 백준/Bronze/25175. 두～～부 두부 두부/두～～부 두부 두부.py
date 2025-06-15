# 1. 전체 인원, 현재 기준점 M, 이동하는 값 K
# 2. 순환형이니까 모듈러 생각해보기
# 3. K가 음수이면 양수가 될 때까지 N 더해주기

N, M, K = map(int, input().split())

while K < 0:
    K += N
    
next_person = M + ((K - 3) % N)
if next_person > N:
    next_person %= N
    
print(next_person)