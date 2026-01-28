a, b = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort()

left, right = 0, 0
cnt = 0
while left < a and right < b:
    if arr_a[left] == arr_b[right]:
        left += 1
        right += 1 
    elif arr_a[left] > arr_b[right]:
        cnt += 1
        right += 1
    else:
        cnt += 1
        left += 1

cnt += a - left + b - right
print(cnt)