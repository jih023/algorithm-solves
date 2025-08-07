x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

circle_dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
radius = (r1 + r2) ** 2

if circle_dist >= radius:
    print('NO')
else:
    print('YES')