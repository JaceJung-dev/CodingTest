import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:       # 탈출조건
        if len(scoville) < 2:    # 개수가 1개 이하이고 K보다 작으면 불가능
            return -1
        
        answer += 1
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        new_food = first_min + second_min * 2
        
        heapq.heappush(scoville, new_food)
    
    return answer