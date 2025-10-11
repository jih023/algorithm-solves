n, m, h = map(int, input().split())
ans = 4

def back_tracking(idx, r, c):
    global board, ans

    possible = True
    for start in range(1, n + 1):
        pos = start
        for i in range(1, h + 1):
            if board[i][pos]:
                pos += 1
            elif board[i][pos - 1]:
                pos -= 1
        
        if pos != start:
            possible = False
            break
    
    if possible:
        ans = min(ans, idx)
        return
    
    if idx == 3 or idx >= ans:
        return
    
    for i in range(r, h + 1):
        k = 1
        if i == r:
            k = c
        for j in range(k, n):
            if not board[i][j] and not board[i][j + 1] and not board[i][j - 1]:
                board[i][j] = True
                back_tracking(idx + 1, i, j)
                board[i][j] = False

board = [[0] * 11 for _ in range(31)]

for i in range(m):
    a, b = map(int, input().split())
    board[a][b] = True

back_tracking(0, 1, 1)

if ans < 4:
    print(ans)
else:
    print(-1)