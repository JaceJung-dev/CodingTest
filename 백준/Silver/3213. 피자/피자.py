import sys
input = sys.stdin.readline

N = int(input())
q, h, t = 0, 0, 0
for _ in range(N):
    s = input().strip()
    if s == "1/4":
        q += 1
    elif s == "1/2":
        h += 1
    else:
        t += 1
        
pizzas = 0

pizzas += t
q -= min(t, q)

pizzas += h // 2
if h % 2:
    pizzas += 1
    q = max(0, q - 2)
    
pizzas += q // 4
if q % 4:
    pizzas += 1
    
print(pizzas)