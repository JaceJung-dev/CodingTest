# 1. 전체 인원, 현재 기준점 M, 이동하는 값 K
# 2. 순환형이니까 modulo 생각해보기
# 3. modulo연산을 사용하려면 0부터 시작하는 index로 바꿔주고 계산
# 4. 순환 계산을 끝낸 후 1-index로 다시 변환해주기

N, M, K = map(int, input().split())

offset = K - 3
next_person = (M + offset - 1) % N + 1
print(next_person)