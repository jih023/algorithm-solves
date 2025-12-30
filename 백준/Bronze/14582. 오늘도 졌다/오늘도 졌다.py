w = list(map(int, input().split()))
s = list(map(int, input().split()))

score_w, score_s = 0, 0
win_w = 0
flag = 0

for i in range(9):
    score_w += w[i]
    if score_w > score_s:
        win_w = 1
    
    score_s += s[i]
    if score_s > score_w and win_w:
        flag = 1

if score_s > score_w and flag:
    print('Yes')
else:
    print('No')