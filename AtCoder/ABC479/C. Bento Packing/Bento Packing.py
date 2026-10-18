n, w = map(int, input().split())

dish = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

def dfs(i, weight, taste):
    global ans

    if i == n:
        ans = max(ans, taste)
        return

    a, b = dish[i]
    dfs(i + 1, weight, taste)
    if weight + b <= w:
        dfs(i + 1, weight + b, taste + a)

dfs(0, 0, 0)
print(ans)