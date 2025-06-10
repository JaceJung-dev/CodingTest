n, q = map(int, input().split())
num_seq = list(map(int, input().split()))
    
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1]-1, query[2]-1
        print(sum(num_seq[a: b+1]))
        temp = num_seq[b]
        num_seq[b] = num_seq[a]
        num_seq[a] = temp
    else:
        a, b, c, d = query[1]-1, query[2]-1, query[3]-1, query[4]-1
        print(sum(num_seq[a:b+1]) - sum(num_seq[c:d+1]))