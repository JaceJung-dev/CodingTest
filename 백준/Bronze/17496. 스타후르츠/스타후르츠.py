N, T, C, P = map(int, input().split())

count = (N - 1) // T
total_income = count * C * P

print(total_income)
