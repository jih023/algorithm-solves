import sys
input = sys.stdin.readline

n = int(input())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

cnt_w = 0
cnt_b = 0

def check_paper(x, y, size):
    global cnt_w, cnt_b
    blue = 0
    white = 0

    for i in range(y, y + size):
        for j in range(x, x + size):
            if not paper[i][j]:
                blue = 1
            elif paper[i][j]:
                white = 1
    
    if not blue:
        cnt_b += 1
    elif not white:
        cnt_w += 1
    else:
        if size >= 2:
            check_paper(x, y, size // 2)
            check_paper(x, y + size // 2, size // 2)
            check_paper(x + size // 2, y, size // 2)
            check_paper(x + size // 2, y + size // 2, size // 2)

check_paper(0, 0, n)
print(cnt_w)
print(cnt_b)