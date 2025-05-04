N = int(input())
t_size = list(map(int,input().split()))
T, P = map(int, input().split())

t_bundle = 0
p_bundle = 0
p_count = 0

for n in t_size:
    if n % T == 0:
        t_bundle += int(n / T)
    else:
        t_bundle += int((n // T) + 1)

p_bundle = N // P
p_count = N % P

print(t_bundle)
print(p_bundle, p_count)