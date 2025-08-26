from collections import deque
import heapq

n, m = map(int, input().split())

fee = [int(input()) for _ in range(n)]
weight = [0] + [int(input()) for _ in range(m)]
order = [int(input()) for _ in range(m * 2)]

waiting = deque()
hq = list(range(n))
heapq.heapify(hq)

result = 0
parking_pos = [0] * (m + 1)
for i in order:
    if i > 0:
        if hq:
            pos = heapq.heappop(hq)
            parking_pos[i] = pos
        else:
            waiting.append(i)
    else:
        pos = parking_pos[-i]
        result += weight[-i] * fee[pos]

        if waiting:
            car = waiting.popleft()
            parking_pos[car] = pos
        else:
            heapq.heappush(hq, pos)

print(result)