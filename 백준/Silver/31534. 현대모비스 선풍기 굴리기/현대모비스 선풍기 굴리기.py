import math

a, b, h = map(int, input().split())

x = b * h / (b - a)
xh = x - h

y = x ** 2 + b ** 2
yh = xh ** 2 + a ** 2

print((y - yh) * math.pi)