def solution(chicken):
    if chicken < 10:
        return 0
    
    service = chicken // 10
    coupon = service + (chicken % 10)
    return service + solution(coupon)