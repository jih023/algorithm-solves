import sys
input = sys.stdin.readline

l, c = map(int, input().split())

chars = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

def backtrack(start_idx, current_pw):
    if len(current_pw) == l:
        vowel_cnt = 0
        consonant_cnt = 0

        for char in current_pw:
            if char in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(current_pw)

        return
    
    for i in range(start_idx, c):
        backtrack(i + 1, current_pw + chars[i])

backtrack(0, "")