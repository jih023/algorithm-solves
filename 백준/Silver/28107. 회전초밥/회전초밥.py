import heapq

n, m = map(int, input().split())

order = [[] for _ in range(200001)]
ans = [0] * 100000

for i in range(n):
    data = list(map(int, input().split()))

    for num in data[1:]:
        heapq.heappush(order[num], i)

sushi = list(map(int, input().split()))

for s in sushi:
    if order[s]:
        customer = heapq.heappop(order[s])
        ans[customer] += 1

print(' '.join(map(str, ans[:n])))