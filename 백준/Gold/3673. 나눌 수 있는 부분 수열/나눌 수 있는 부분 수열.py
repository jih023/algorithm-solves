for _ in range(int(input())):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sum_arr = [arr[0] % d]
    for i in range(1, n):
        sum_arr.append((sum_arr[-1] + arr[i]) % d)

    count_arr = [0] * 1000001
    count_arr[0] += 1
    for i in sum_arr:
        count_arr[i] += 1
    
    result = 0
    for i in count_arr:
        if i >= 2:
            result += ((i * (i - 1)) // 2)
    
    print(result)