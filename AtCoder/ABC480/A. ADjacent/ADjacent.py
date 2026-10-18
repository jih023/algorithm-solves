st = list(input() for _ in range(2))
if (st[0][0] in 'AD' and st[1][1] in 'AD') or (st[0][1] in 'AD' and st[1][0] in 'AD'):
    print('No')
else:
    print('Yes')