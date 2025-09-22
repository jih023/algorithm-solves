n = int(input())

candy = []
for _ in range(n):
    candy.append(list(input()))

max_num = 0
for i in range(n):
    for j in range(n):
        if j < n-1:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

            color, cnt = candy[i][0], 1
            for k in range(1, n):
                if candy[i][k] == color:
                    cnt += 1
                else:
                    max_num = max(max_num, cnt)
                    color, cnt = candy[i][k], 1
            max_num = max(max_num, cnt)

            color, cnt = candy[0][j], 1
            for k in range(1, n):
                if candy[k][j] == color:
                    cnt += 1
                else:
                    max_num = max(max_num, cnt)
                    color, cnt = candy[k][j], 1
            max_num = max(max_num, cnt)

            color, cnt = candy[0][j+1], 1
            for k in range(1, n):
                if candy[k][j+1] == color:
                    cnt += 1
                else:
                    max_num = max(max_num, cnt)
                    color, cnt = candy[k][j+1], 1
            max_num = max(max_num, cnt)

            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        if i < n-1:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

            color, cnt = candy[i][0], 1
            for k in range(1, n):
                if candy[i][k] == color:
                    cnt += 1
                else:
                    max_num = max(max_num, cnt)
                    color, cnt = candy[i][k], 1
            max_num = max(max_num, cnt)

            color, cnt = candy[i+1][0], 1
            for k in range(1, n):
                if candy[i+1][k] == color:
                    cnt += 1
                else:
                    max_num = max(max_num, cnt)
                    color, cnt = candy[i+1][k], 1
            max_num = max(max_num, cnt)

            color, cnt = candy[0][j], 1
            for k in range(1, n):
                if candy[k][j] == color:
                    cnt += 1
                else:
                    max_num = max(max_num, cnt)
                    color, cnt = candy[k][j], 1
            max_num = max(max_num, cnt)

            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(max_num)