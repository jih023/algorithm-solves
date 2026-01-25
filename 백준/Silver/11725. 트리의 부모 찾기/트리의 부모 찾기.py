from collections import deque

n = int(input())
adj = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque()
visited = [0] * (n + 1)
visited[1] = 1
q.append(1)
result = [0] * (n + 1)

while q:
    num = q.popleft()
    for i in adj[num]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
            result[i] = num 

for i in range(2, n + 1):
    print(result[i])