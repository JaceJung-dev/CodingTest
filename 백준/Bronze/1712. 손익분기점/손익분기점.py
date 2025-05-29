fixed_cost, variable_cost, selling_cost = map(int,input().split())

try:
    break_even_point = fixed_cost / (selling_cost - variable_cost)
    if break_even_point < 0:
        print(-1)
    else:
        print(int(break_even_point)+1)
except:
    print(-1)