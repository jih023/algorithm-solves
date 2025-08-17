import sys
sys.setrecursionlimit(300000)

n, m, r = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

adj = [sorted(row, reverse=True) for row in adj]

idx, cnt = 1, 1
visited = [0] * (n + 1)
visited[r] = 1

def dfs(n):
    global idx, cnt
    global visited

    for i in adj[n]:
        if not visited[i]:
            cnt += 1
            visited[i] = cnt
            dfs(i)

dfs(r)
for i in range(n):
    print(visited[i+1])