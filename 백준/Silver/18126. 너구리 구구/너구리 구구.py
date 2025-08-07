import sys
sys.setrecursionlimit(25000000)

n = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

visited = [0] * (n + 1)
visited[1] = 1
max_dist = 0

def dfs(m, dist):
    global max_dist
    global visited
    for i, j in adj[m]:
        if not visited[i]:
            max_dist = max(max_dist, dist + j)
            visited[i] = 1
            dfs(i, dist + j)

dfs(1, 0)
print(max_dist)