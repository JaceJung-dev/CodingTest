max_num = 0
max_count = 0
count = 0
while True:
    try:
        num = int(input())
        count += 1
        if num > max_num:
            max_num = num
            max_count = count
    except:
        break

print(max_num)
print(max_count)