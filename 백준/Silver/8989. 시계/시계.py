for _ in range(int(input())):
    time = list(input().split())
    ans = []

    for i in time:
        h, m = map(int, i.split(':'))

        pos_h = h % 12
        pos_h = pos_h * 60 + m
        pos_m = m * 12

        angle = abs(pos_h - pos_m)
        angle = min(angle, 720 - angle)
        
        ans.append((angle, h, m, i))
    
    ans.sort(key=lambda x: (x[0], x[1], x[2]))

    print(ans[2][3])