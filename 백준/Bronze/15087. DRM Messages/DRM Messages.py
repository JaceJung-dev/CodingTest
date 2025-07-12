import sys
input = sys.stdin.readline

def get_rotate_num(word):
    rotate_num = 0
    for char in word:
        char_value = ord(char) - ord("A")
        rotate_num += char_value
    return rotate_num

def get_rotated_word(word, rotate_num):
    rotated_word = ""
    for char in word:
        forward_moved = (ord(char) - ord("A") + rotate_num) % 26 + ord("A")
        rotated_word += chr(forward_moved)
    return rotated_word

def get_merged_word(front, back):
    merged_word = ""
    for i in range(len(front)):
        rotate_num = ord(back[i]) - ord("A")
        forward_moved = (ord(front[i]) - ord("A") + rotate_num) % 26 + ord("A")
        merged_word += chr(forward_moved)
    return merged_word
    
    
N = input().strip()
half = len(N) // 2
front, back = N[:half], N[half:]

front_rotate_num = get_rotate_num(front)
back_rotate_num = get_rotate_num(back)
  
front_rotated_word = get_rotated_word(front, front_rotate_num)
back_rotated_word = get_rotated_word(back, back_rotate_num)

print(get_merged_word(front_rotated_word, back_rotated_word))
