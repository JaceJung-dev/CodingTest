def solution(spell, dic):
    spell = set(spell)
    for char in dic:
        if not spell - set(char):
            return 1
    return 2