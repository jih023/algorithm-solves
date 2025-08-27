import heapq

n, p, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

INF = int(1e9)
distance = [[INF] * (n + 1) for _ in range(n + 1)]

def dijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, (start, 0)))
    distance[start][0] = 0

    while q:
        cost, (x, free_cnt) = heapq.heappop(q)

        if distance[x][free_cnt] < cost:
            continue

        for i in adj[x]:
            nx, nc = i[0], i[1]

            if cost < nc:
                if free_cnt < k:
                    if distance[nx][free_cnt + 1] > cost:
                        heapq.heappush(q, (cost, (nx, free_cnt + 1)))
                        distance[nx][free_cnt + 1] = cost
                
                if distance[nx][free_cnt] > nc:
                    heapq.heappush(q, (nc, (nx, free_cnt)))
                    distance[nx][free_cnt] = nc
            
            else:
                if distance[nx][free_cnt] > cost:
                    heapq.heappush(q, (cost, (nx, free_cnt)))
                    distance[nx][free_cnt] = cost

dijkstra(1)

ans = INF
for i in range(n):
    ans = min(ans, distance[n][i])

if ans == INF:
    print(-1)
else:
    print(ans)