n = int(input())
strong = list(map(int, input().split()))

max_num = 0
max_num_idx = []
for i in range(n):
    if strong[i] > max_num:
        max_num = strong[i]
        max_num_idx = [i]
    elif strong[i] == max_num:
        max_num_idx.append(i)

middle = n // 2 - 0.5
left_dist = middle - max_num_idx[0]
right_dist = max_num_idx[-1] - middle

if left_dist == right_dist:
    print('X')
elif left_dist > right_dist:
    print('R')
else:
    print('B')