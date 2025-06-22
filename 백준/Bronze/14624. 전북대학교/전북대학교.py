N = int(input())

if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print("*" * N)
    half = (N - 1) // 2
    print(" " * half + "*")

    for i in range(1, half + 1):
        print(" " * (half - i) + "*" + " " * (2 * i - 1) + "*")  
           
       