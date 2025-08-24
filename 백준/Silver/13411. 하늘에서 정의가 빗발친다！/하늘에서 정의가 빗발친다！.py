n = int(input())

missile = []
for i in range(n):
    x, y, v = map(int, input().split())
    missile.append(((x ** 2 + y ** 2) ** 0.5 / v, i + 1))

missile.sort(key=lambda x: x[0])

for m in missile:
    print(m[1])