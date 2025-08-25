from collections import deque

s = int(input())

visited = [[0] * (s * 2 + 1) for _ in range(s * 2 + 1)]
q = deque()
visited[1][0] = 1
q.append((1, 0, 0))

while q:
    num, clip, time = q.popleft()

    if num == s:
        print(time)
        break

    # cmd 1
    if not visited[num][num]:
        visited[num][num] = 1
        q.append((num, num, time + 1))

    # cmd 2
    if clip > 0 and num + clip <= s * 2 and not visited[num + clip][clip]:
        visited[num + clip][clip] = 1
        q.append((num + clip, clip, time + 1))

    # cmd 3
    if num >= 1:
        if not visited[num - 1][clip]:
            visited[num - 1][clip] = 1
            q.append((num - 1, clip, time + 1))