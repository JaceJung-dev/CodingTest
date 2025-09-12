# https://stackoverflow.com/questions/46331714/possible-combination-of-a-nested-list-in-python
# https://stackoverflow.com/questions/13675296/how-to-overcome-typeerror-unhashable-type-list

import itertools

def is_match(full_id, ban_id):
    if len(full_id) != len(ban_id):
        return False
    
    for i in range(len(full_id)):
        if ban_id[i] != "*" and ban_id[i] != full_id[i]:
            return False
    
    return True

def solution(user_id, banned_id):
    answer = 0
    # 1. banned_id 별로 진짜 banned_id에 들어갈 수 있는 아이디 리스트
    candidates = []
    
    for b_id in banned_id:
        cand = []
        for u in user_id:
            if is_match(u, b_id):
                cand.append(u)
        
        # banned_id 리스트에 있는 아이디랑 맞는 user_id 없는 경우
        if not cand:
            return 0
                
        candidates.append(cand)
    
    # banned_id 별로 구분된 리스트에서 하나씩 뽑아서 모든 경우의 수 만들기
    all_possibility = list(itertools.product(*candidates))
    
    final = set()
    for pos in all_possibility:
        
        # 같은 아이디를 뽑은 경우 제거
        if len(pos) != len((set(pos))):
            continue
        
        final.add(tuple(sorted(pos))) # TypeError: unhashable type: 'list' -> nested tuple로 쓸 것

    return len(final)
