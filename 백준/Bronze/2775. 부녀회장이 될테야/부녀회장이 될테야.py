import sys
input = sys.stdin.readline
    
T = int(input())

for _ in range(T):
    floor = int(input().strip())
    room = int(input().strip())
    
    people = [num for num in range(1, room + 1)]
    
    for i in range(1, floor+1):
        temp = []
        for j in range(room):
            temp.append(sum(people[:j+1]))
        people = temp
        
    print(people[-1])
