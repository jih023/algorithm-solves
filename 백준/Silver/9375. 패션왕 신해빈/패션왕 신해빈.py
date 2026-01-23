n = int(input())

for _ in range(n):
    m = int(input())

    d = {}

    for _ in range(m):
        a, b = input().split()

        d.setdefault(b, 0)
        d[b] += 1

    result = 1
    for v in d.values():
        result *= (v + 1)

    print(result - 1)