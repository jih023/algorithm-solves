for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    check1 = (r1 + r2) ** 2
    check2 = (r1 - r2) ** 2
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif distance > check1 or distance < check2:
        print(0)
    elif distance == check1 or distance == check2:
        print(1)
    else:
        print(2)