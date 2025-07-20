n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

merged_arr1 = []
merged_arr2 = []

for i in range(n):
    for j in range(n):
        merged_arr1.append(arr[i][0] + arr[j][1])
        merged_arr2.append(arr[i][2] + arr[j][3])

merged_arr1.sort()
merged_arr2.sort()

cnt = 0
left, right = 0, n * n - 1
while left < n * n and right >= 0:
    total = merged_arr1[left] + merged_arr2[right]

    if total == 0:
        left_value = merged_arr1[left]
        right_value = merged_arr2[right]
        left_num = 0
        right_num = 0
        while left < n * n and merged_arr1[left] == left_value:
            left += 1
            left_num += 1
        while right >= 0 and merged_arr2[right] == right_value:
            right -= 1
            right_num += 1
        cnt += left_num * right_num
    elif total < 0:
        left += 1
    else:
        right -= 1

print(cnt)