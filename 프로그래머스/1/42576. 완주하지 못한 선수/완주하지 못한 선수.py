def solution(participant, completion):
    marathon = {}
    hash_sum = 0
    
    for person in participant:
        marathon[hash(person)] = person
        hash_sum += hash(person)
        
    for person in completion:
        hash_sum -= hash(person)
        
    answer = marathon[hash_sum]
    return answer