N = int(input())
items = []
for _ in range(N):
    item = float(input())
    items.append(item)
    
items.sort()
second_item = items[1]
print(format(second_item, ".2f"))
