n, x, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0
end = 0

for i in a:
    if i >= t:
        break

    if i > end:
        cnt = (i - end + x - 1) // x
        ans += cnt
        end += cnt * x

    end = max(end, i + x)

if end < t:
    ans += (t - end + x - 1) // x

print(ans)