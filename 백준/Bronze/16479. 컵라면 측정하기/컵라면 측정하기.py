k = int(input())
d1, d2 = map(int, input().split())

result = k ** 2 - (d1 - d2) ** 2 / 4

print(result)