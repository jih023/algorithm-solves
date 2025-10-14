n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 1000001
for i in a:
    cnt[i] += 1

ans = [-1] * n
s = []
for i in range(n):
    while s and cnt[a[s[-1]]] < cnt[a[i]]:
        ans[s[-1]] = a[i]
        s.pop()
    s.append(i)

print(*ans)