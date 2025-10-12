from collections import deque

n, m = map(int, input().split())

home = deque()
chicken = []
chicken_cnt = 0
ans = int(1e9)
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(len(num)):
        if num[j] == 1:
            home.append((i, j))
        elif num[j] == 2:
            chicken.append(((i, j), True))
            chicken_cnt += 1

def back_tracking(idx, chicken_idx):
    global chicken, ans

    total_dist = 0
    for i, j in home:
        dist = int(1e9)
        for (x, y), check in chicken:
            if check:
                dist = min(dist, abs(i - x) + abs(j - y))
        total_dist += dist
    
    if chicken_cnt - idx <= m or total_dist >= ans:
        ans = min(ans, total_dist)
        return
    
    for i in range(chicken_idx, len(chicken)):
        pos, flag = chicken[i]
        chicken[i] = (pos, False)

        back_tracking(idx + 1, i + 1)

        chicken[i] = (pos, True)

back_tracking(0, 0)
print(ans)