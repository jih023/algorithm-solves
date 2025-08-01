n = int(input())

n_arr = []
p_arr = []
zero_cnt = 0
for _ in range(n):
    i = int(input())
    if i < 0:
        n_arr.append(i)
    elif i == 0:
        zero_cnt += 1
    else:
        p_arr.append(i)

n_arr.sort()
p_arr.sort()

ans = 0

while len(n_arr) > 1:
    first = n_arr.pop(0)
    second = n_arr.pop(0)
    ans += first * second

if n_arr:
    if not zero_cnt:
        ans += n_arr[0]
        
while (p_arr):
    first = p_arr.pop()
    
    if (not p_arr):
        ans += first
        break

    second = p_arr.pop()

    if first != 1 and second != 1:
        ans += first * second
    else:
        ans += first + second

print(ans)