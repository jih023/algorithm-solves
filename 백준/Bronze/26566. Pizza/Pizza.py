import math

for _ in range(int(input())):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())

    pizza1 = a1 / p1
    pizza2 = (r1 ** 2) * math.pi / p2

    if pizza1 < pizza2:
        print("Whole pizza")
    else:
        print("Slice of pizza")