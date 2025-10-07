v = []

def back_tracking(idx):
    global sudoku
    
    if idx == len(v):
        return True
    
    i, j = v[idx]
    area_i = i // 3 * 3
    area_j = j // 3 * 3

    for n in range(1, 10):
        possible = True
        
        for m in range(9):
            if sudoku[i][m] == n or sudoku[m][j] == n:
                possible = False
                break
        
        for r in range(area_i, area_i + 3):
            for c in range(area_j, area_j + 3):
                if sudoku[r][c] == n:
                    possible = False
                    break
            if not possible:
                break
        
        if possible:
            sudoku[i][j] = n
            if back_tracking(idx + 1):
                return True
            sudoku[i][j] = 0
    
    return False

sudoku = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            v.append((i, j))

back_tracking(0)

for row in sudoku:
    print(" ".join(map(str, row)))