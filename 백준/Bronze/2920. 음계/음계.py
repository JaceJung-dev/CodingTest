check_list = list(map(int, input().split()))

if check_list == sorted(check_list):
    print("ascending")
elif check_list == sorted(check_list, reverse=True):
    print("descending")
else:
    print("mixed")