n = input()
compare_num = ""
num = 1


while len(compare_num) < len(n):
    compare_num += str(num)
    num += 1

if n == compare_num:
    print(num - 1)
else:
    print(-1)