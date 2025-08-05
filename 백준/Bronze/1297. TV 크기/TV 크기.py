import math

d, h, w = map(int, input().split())

k2 = d ** 2 / (w ** 2 + h ** 2)
k = math.sqrt(k2)

print(int(k * h), int(k * w))