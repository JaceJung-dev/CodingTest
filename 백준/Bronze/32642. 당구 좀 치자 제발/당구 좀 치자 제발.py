N = int(input())
weather = list(map(int, input().split()))
total_rage = 0
rage  = 0
for i in weather:
    if i == 0:
        rage -= 1
    else:
        rage += 1
    total_rage += rage
print(total_rage)