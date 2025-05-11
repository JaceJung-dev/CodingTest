def solution(id_pw, db):
    answer = ''
    for user in db:
        user_id, user_pw = user[0], user[1]
        if user_id == id_pw[0]:
            if user_pw == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"