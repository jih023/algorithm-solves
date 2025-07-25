n = int(input())
hongjun = list(input())

arr = [['#' for _ in range(2 * n)] for _ in range(2 * n)]

x, y = n - 1, n - 1
arr[y][x] = '.'

# 0남쪽 1서쪽 2북쪽 3동쪽
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
direction = 0

max_x, max_y, min_x, min_y = x, y, x, y

for i in hongjun:
    if i == 'F':
        x += dx[direction]
        y += dy[direction]
        arr[y][x] = '.'
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    elif i == 'R':
        direction += 1
        direction %= 4
    else:
        direction -= 1
        direction %= 4

for i in range(min_y, max_y + 1):
    for j in range(min_x, max_x + 1):
        print(arr[i][j], end="")
    print()