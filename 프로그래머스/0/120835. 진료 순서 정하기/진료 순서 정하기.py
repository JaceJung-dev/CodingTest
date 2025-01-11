def solution(emergency):
    order_dict = { v : i + 1 for i, v in enumerate(sorted(emergency, reverse=True))}
    answer = [order_dict[e] for e in emergency]
    return answer