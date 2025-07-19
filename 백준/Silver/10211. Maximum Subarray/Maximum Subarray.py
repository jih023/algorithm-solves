for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    
    max_sum = x[0]
    current_sum = x[0]

    for i in range(1, n):
        current_sum = max(x[i], current_sum + x[i])
        max_sum = max(max_sum, current_sum)
    
    print(max_sum)