n = int(input())
s = list(input())

max_day, day = 0, 0
for i in range(n):
    if s[i] == 'R':
        day += 1
        max_day = max(max_day, day)
    else:
        day = 0

print(max_day)