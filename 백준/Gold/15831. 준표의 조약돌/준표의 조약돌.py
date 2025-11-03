n, b, w = map(int, input().split())
stones = input().strip()

left = 0
black, white = 0, 0
max_len = 0

for right in range(n):
    if stones[right] == 'B':
        black += 1
    else:
        white += 1

    while black > b:
        if stones[left] == 'B':
            black -= 1
        else:
            white -= 1
        left += 1
    
    if white >= w:
        max_len = max(max_len, right - left + 1)

print(max_len)