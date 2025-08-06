import sys
input = sys.stdin.readline

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    px, py = points[i]
    vectors = []

    for j in range(n):
        if i == j:
            continue
        x, y = points[j]
        dx, dy = x - px, y - py
        vectors.append((dx, dy))

    for a in range(len(vectors)):
        for b in range(a + 1, len(vectors)):
            dx1, dy1 = vectors[a]
            dx2, dy2 = vectors[b]
            if dx1 * dx2 + dy1 * dy2 == 0:
                cnt += 1

print(cnt)