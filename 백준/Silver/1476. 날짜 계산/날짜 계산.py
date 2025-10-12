e, s, m = map(int, input().split())

for i in range(1, 15 * 28 * 19 + 1):
    if (i - 1) % 15 + 1 == e and (i - 1) % 28 + 1 == s and (i - 1) % 19 + 1 == m:
        print(i)
        break