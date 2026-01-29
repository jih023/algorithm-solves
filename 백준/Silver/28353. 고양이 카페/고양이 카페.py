n, k = map(int, input().split())
w = list(map(int, input().split()))

w.sort()
left, right = 0, n - 1

cnt = 0
while left < right:
    if w[left] + w[right] <= k:
        cnt += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(cnt)