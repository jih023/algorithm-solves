n, w, h = map(int, input().split())

max_length = (w ** 2 + h ** 2) ** 0.5
for _ in range(n):
    m = int(input())
    if m <= max_length:
        print('DA')
    else:
        print('NE')