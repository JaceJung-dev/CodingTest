N = input()
num_list = [0] * 5

for num in N:
    if int(num) in [0, 1, 2]:
        num_list[int(num)] += 1
    elif int(num) == 8:
        num_list[3] += 1
    else:
        num_list[4] += 1

def is_related(num_list):
    if num_list[0] * num_list[1] * num_list[2] * num_list[3] != 0:
        return True
    return False

def is_tied(num_list):
    start_num = num_list[0]
    for i in range(4):
        if num_list[i] != start_num:
            return False
    return True
    
    
if num_list[4] != 0:
    print(0)
elif num_list[4] == 0 and is_related and is_tied(num_list):
    print(8)
elif num_list[4] == 0 and is_related(num_list):
    print(2)
else:
    print(1)

