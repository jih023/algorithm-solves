import heapq

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

INF = int(1e9)
parent = [0] * (n + 1)

def dijkstra(start):
    global parent
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                parent[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

print(n-1)
for i in range(2, n + 1):
    print(i, parent[i])