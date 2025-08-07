import sys
sys.setrecursionlimit(200000)

v = int(input())

adj = [[] for _ in range(v + 1)]
for _ in range(v):
    readline = list(map(int, input().split()))
    for i in range(len(readline) // 2 - 1):
        adj[readline[0]].append((readline[2 * i + 1], readline[2 * i + 2]))
        adj[readline[2 * i + 1]].append((readline[0], readline[2 * i + 2]))

idx, max_dist = 1, 0
visited = [0] * (v + 1)
visited[1] = 1

def dfs(n, dist):
    global idx, max_dist
    global visited

    for i, j in adj[n]:
        if not visited[i]:
            visited[i] = 1
            sum_dist = dist + j
            if sum_dist > max_dist:
                max_dist = sum_dist
                idx = i
            dfs(i, dist + j)

dfs(1, 0)
visited = [0] * (v + 1)
visited[idx] = 1
dfs(idx, 0)

print(max_dist)