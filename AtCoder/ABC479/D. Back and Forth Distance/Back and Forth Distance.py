n, q = map(int, input().split())

INF = float("inf")
l = [INF, INF] + list(map(int, input().split()))
r = [INF] + list(map(int, input().split())) + [INF]

left_min = [INF] * (n + 1)
right_min = [INF] * (n + 2)

for i in range(1, n + 1):
    left_min[i] = min(left_min[i - 1], r[i])

for i in range(n, 0, -1):
    right_min[i] = min(right_min[i + 1], l[i])

for _ in range(q):
    a, b = map(int, input().split())

    if a < b:
        ans = r[a]
        if a > 1:
            ans = min(ans, l[a] + left_min[a - 1])
    else:
        ans = l[a]
        if a < n:
            ans = min(ans, r[a] + right_min[a + 1])

    print(ans)