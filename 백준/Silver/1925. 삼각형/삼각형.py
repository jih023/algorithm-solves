x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = (x2 - x3) ** 2 + (y2 - y3) ** 2
b = (x1 - x3) ** 2 + (y1 - y3) ** 2
c = (x1 - x2) ** 2 + (y1 - y2) ** 2

sides = [a, b, c]
sides.sort()

if (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1):
    print('X')
elif a == b and b == c:
    print('JungTriangle')
elif a == b or b == c or a == c:
    if sides[0] + sides[1] == sides[2]:
        print('Jikkak2Triangle')
    elif sides[0] + sides[1] < sides[2]:
        print('Dunkak2Triangle')
    else:
        print('Yeahkak2Triangle')
else:
    if sides[0] + sides[1] == sides[2]:
        print('JikkakTriangle')
    elif sides[0] + sides[1] < sides[2]:
        print('DunkakTriangle')
    else:
        print('YeahkakTriangle')