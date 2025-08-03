from collections import defaultdict

r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]
r_num, c_num = 3, 3

time = 0
while time <= 100:
    if r - 1 < r_num and c - 1 < c_num and arr[r - 1][c - 1] == k:
        print(time)
        break

    time += 1

    if r_num >= c_num:  # R 연산
        new_arr = []
        max_len = 0
        for i in range(r_num):
            counter = defaultdict(int)
            for j in range(c_num):
                if arr[i][j] != 0:
                    counter[arr[i][j]] += 1

            sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

            new_row = []
            for a, b in sorted_items:
                new_row.extend([a, b])
            max_len = max(max_len, len(new_row))
            new_arr.append(new_row)

        # 길이 맞춰주기 (0으로 채움)
        for row in new_arr:
            while len(row) < max_len:
                row.append(0)
            if len(row) > 100:
                row[:] = row[:100]

        arr = new_arr
        c_num = min(100, max_len)

    else:  # C 연산
        new_arr = []
        max_len = 0
        for j in range(c_num):
            counter = defaultdict(int)
            for i in range(r_num):
                if arr[i][j] != 0:
                    counter[arr[i][j]] += 1

            sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

            new_col = []
            for a, b in sorted_items:
                new_col.extend([a, b])
            max_len = max(max_len, len(new_col))
            new_arr.append(new_col)

        # 2차원 배열로 바꾸기 (열들을 행으로)
        temp = [[0] * c_num for _ in range(min(100, max_len))]
        for j in range(c_num):
            for i in range(len(new_arr[j])):
                if i >= 100:
                    break
                temp[i][j] = new_arr[j][i]

        arr = temp
        r_num = min(100, max_len)

else:
    print(-1)