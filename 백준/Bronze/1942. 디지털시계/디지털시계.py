import sys
input = sys.stdin.readline

for _ in range(3):
    start_time, end_time = input().split()
    s_hour, s_min, s_sec = map(int, start_time.split(":"))
    e_hour, e_min, e_sec = map(int, end_time.split(":"))
    
    count = 0
    while True:
        if s_sec == 60:
            s_min += 1
            s_sec = 0
        if s_min == 60:
            s_hour += 1
            s_min = 0
        if s_hour == 24:
            s_hour = 0
            
        time_int = s_hour * 10000 + s_min * 100 + s_sec
        
        if time_int % 3 == 0:
            count += 1
            
        if (s_hour == e_hour) and (s_min == e_min) and (s_sec == e_sec):
            break
            
        s_sec += 1

    print(count)        