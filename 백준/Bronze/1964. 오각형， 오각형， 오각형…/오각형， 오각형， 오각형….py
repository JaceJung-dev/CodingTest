N = int(input())

result = 5
for i in range(2, N+1):
    result += (3 * i + 1)

print(result % 45678)