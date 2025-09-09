def solution(phone_book):
    phone_book.sort()
    i = 1
    while i < len(phone_book):
        prefix = phone_book[i - 1]
        
        if phone_book[i].startswith(prefix):
            return False
        
        i += 1
        
    return True