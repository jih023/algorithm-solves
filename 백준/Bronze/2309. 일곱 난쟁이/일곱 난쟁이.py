arr = list(int(input()) for _ in range(9))
arr.sort()
arr_sum = sum(arr)
diff = arr_sum - 100

for i in range(8):
    for j in range(i + 1, 9):
        if arr[i] + arr[j] == diff:
            a, b = arr[i], arr[j]
            result = [x for x in arr if x != a and x != b]
            for x in result:
                print(x)
            exit()