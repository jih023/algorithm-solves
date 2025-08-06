w, h, x, y, p = map(int, input().split())

cnt = 0
for _ in range(p):
    a, b = map(int, input().split())
    if x <= a <= x + w and y <= b <= y + h:
        cnt += 1
    else:
        check1 = (x - a) ** 2 + (y + h / 2 - b) ** 2
        check2 = (x + w - a) ** 2 + (y + h / 2 - b) ** 2
        if check1 <= (h ** 2) / 4 or check2 <= (h ** 2) / 4:
            cnt += 1

print(cnt)