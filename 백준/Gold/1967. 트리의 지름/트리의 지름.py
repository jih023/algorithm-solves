import sys
sys.setrecursionlimit(30000)

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

idx, max_dist = 1, 0
visited = [0] * (n + 1)
visited[1] = 1

def dfs(m, dist):
    global idx, max_dist
    global visited

    for i, j in adj[m]:
        if not visited[i]:
            sum_dist = dist + j
            visited[i] = 1
            if sum_dist > max_dist:
                max_dist = sum_dist
                idx = i
            dfs(i, dist + j)

dfs(1, 0)
visited = [0] * (n + 1)
visited[idx] = 1
max_dist = 0
dfs(idx, 0)
print(max_dist)