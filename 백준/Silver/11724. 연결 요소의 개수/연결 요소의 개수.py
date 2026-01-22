from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (n + 1)

cnt = 0
q = deque()

for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = 1
        cnt += 1
        q.append(i)

        while q:
            num = q.popleft()
            for j in adj[num]:
                if not visited[j]:
                    visited[j] = 1
                    q.append(j)

print(cnt)