import sys
input = sys.stdin.readline

N = int(input())
count = 0

def is_winning_ticket(num_string):
    winning_num = "2023"
    i = 0
    for digit in num_string:
        if digit == winning_num[i]:
            i += 1
            if i == 4:
                return True
    return False

for num in range(1000, N + 1):
    if is_winning_ticket(str(num)):
        count += 1
print(count)
