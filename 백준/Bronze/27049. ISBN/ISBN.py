import sys
input = sys.stdin.readline

code = input()
total_sum = 0
multiply_num = 0

def find_missing_num(n):
    for i in range(n):
        temp_sum = total_sum
        temp_sum += i * multiply_num
        if temp_sum % 11 == 0:
            if i == 10:
                return "X"
            else:
                return i
    return -1

for i in range(len(code)):
    try:
        total_sum += int(code[i]) * (10 - i)
    except ValueError:
        if code[i] == "X":
            total_sum += 10
        elif code[i] == "?":
            multiply_num = 10 - i

missing_num = 0

if multiply_num == 1:
    missing_num = find_missing_num(11)
else:
    missing_num = find_missing_num(10)

print(missing_num)