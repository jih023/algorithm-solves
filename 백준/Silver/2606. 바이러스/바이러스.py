from collections import deque

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (n + 1)

cnt = 0
visited[1] = 1
q = deque()
q.append(1)
while q:
    num = q.popleft()
    for i in adj[num]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
            cnt += 1

print(cnt)