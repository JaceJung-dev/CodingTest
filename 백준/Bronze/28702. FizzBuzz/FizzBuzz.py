import sys
input = sys.stdin.readline

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
    
num_seq = [input().rstrip() for _ in range(3)]

i = 0
for num in num_seq:
    if num.isdigit():
        i = num_seq.index(num)
        break

next_num = FizzBuzz(int(num_seq[i]) + (3 - i))
print(next_num)


    