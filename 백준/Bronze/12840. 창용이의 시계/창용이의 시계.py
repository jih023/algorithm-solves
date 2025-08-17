h, m, s = map(int, input().split())

for _ in range(int(input())):
    q = input()
    if q == '3':
        print(h, m, s)
    else:
        t, num = q.split()
        num = int(num)

        total = h * 3600 + m * 60 + s

        if t == '1': 
            total += num
        elif t == '2': 
            total -= num

        total %= 86400

        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60