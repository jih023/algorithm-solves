import heapq

v, e, p = map(int, input().split())

adj = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (v + 1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for nxt, w in adj[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
        
    return distance

dist_from_start = dijkstra(1)
dist_from_p = dijkstra(p)

cost1 = dist_from_start[p]  
cost2 = dist_from_start[v]  
cost3 = dist_from_p[v]  

if cost2 == cost1 + cost3:
    print("SAVE HIM")
else:
    print("GOOD BYE")