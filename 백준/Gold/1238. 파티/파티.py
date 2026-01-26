import heapq

def dijkstra(start, graph):
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
            
        for nxt, w in graph[node]:
            if dist[nxt] > cost + w:
                dist[nxt] = cost + w
                heapq.heappush(pq, (dist[nxt], nxt))
    
    return dist

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
    rev_graph[a].append((b, c))

result1 = dijkstra(x, graph)
result2 = dijkstra(x, rev_graph)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, result1[i] + result2[i])

print(ans)