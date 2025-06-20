N = int(input())
P = int(input())
final_price = 0

if N >= 20:
    if P * 0.25 > 2000:
        final_price = P * 0.75
    else:
        final_price = P - 2000
elif N >= 15:
    if P * 0.1 > 2000:
        final_price = P * 0.9
    else:
        final_price = P - 2000
elif N >= 10:
    if P * 0.1 > 500:
        final_price = P * 0.9
    else:
        final_price = P - 500
elif N >=5:
    final_price = P - 500
else:
    final_price = P
    
if final_price < 0:
    print(0)
else:
    print(int(final_price))