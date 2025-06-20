N = int(input())
P = int(input())

discount_price = [0]

if N >= 5:
    discount_price.append(500)
if N >= 10:
    discount_price.append(int(P * 0.1))
if N >= 15:
    discount_price.append(2000)
if N >= 20:
    discount_price.append(int(P * 0.25))

final_price = P - max(discount_price)

if final_price < 0:
    print(0)
else:
    print(final_price)
