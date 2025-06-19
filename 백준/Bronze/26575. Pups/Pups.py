n = int(input())

for _ in range(n):
    d, f, p = map(float, input().split())
    total = d * f * p
    print(f"${total:.2f}")