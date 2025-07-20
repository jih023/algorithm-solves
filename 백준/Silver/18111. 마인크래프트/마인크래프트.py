n, m, b = map(int, input().split())

block = []
for _ in range(n):
    block.append(list(map(int, input().split())))

min_time = 1e9
max_height = -1

for height in range(257):
    job_one_cnt = 0
    job_two_cnt = 0

    for i in range(n):
        for j in range(m):
            if block[i][j] > height:
                job_one_cnt += (block[i][j] - height)
            elif block[i][j] < height:
                job_two_cnt += (height - block[i][j])
    
    if b - (job_two_cnt - job_one_cnt) >= 0:
        if min_time >= (job_one_cnt * 2 + job_two_cnt):
            min_time = job_one_cnt * 2 + job_two_cnt
            max_height = height

print(min_time, max_height)