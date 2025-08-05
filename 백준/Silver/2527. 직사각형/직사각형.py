for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    left = max(x1, x3)
    right = min(x2, x4)
    bottom = max(y1, y3)
    top = min(y2, y4)

    width = right - left
    height = top - bottom

    if width < 0 or height < 0:
        print('d')  
    elif width == 0 and height == 0:
        print('c')  
    elif width == 0 or height == 0:
        print('b') 
    else:
        print('a') 