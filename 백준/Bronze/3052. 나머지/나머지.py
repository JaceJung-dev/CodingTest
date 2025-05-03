num_list = []
while True:
    try:
        num_list.append(int(input()) % 42)
    except:
        break
        
print(len(set(num_list)))