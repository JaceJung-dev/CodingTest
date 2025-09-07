import sys
input = sys.stdin.readline

def find_end_num(num):
    if num == 0:
        return "INSOMNIA"
    
    num_list = set()
    j = 1
    
    while True:
        N = j * num
        for n in str(N):
            num_list.add(int(n))
            
        if len(num_list) == 10:
            break
            
        j += 1
        
    return N
                
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    end_num = find_end_num(N)
    
    print(f"Case #{i}: {end_num}")