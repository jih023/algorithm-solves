import heapq

n, m = map(int, input().split())

bridge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))

start, end = map(int, input().split())

def dijkstra(s):
    distance = [0] * (n + 1)
    q = []
    heapq.heappush(q, (-1e9, s))  

    while q:
        dist, now = heapq.heappop(q)
        dist = -dist  

        if distance[now] >= dist:
            continue
        distance[now] = dist

        for next_node, weight in bridge[now]:
            new_dist = min(dist, weight)
            if distance[next_node] < new_dist:
                heapq.heappush(q, (-new_dist, next_node))

    return distance[end]

result = dijkstra(start)
print(int(result) if result != 0 else -1)