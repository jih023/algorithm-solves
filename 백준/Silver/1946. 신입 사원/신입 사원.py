t = int(input())

for _ in range(t):
    n = int(input())
    li = []
    for i in range(n):
        row = list(map(int, input().split()))
        li.append(row)
    
    li.sort()
    count = 0
    min = li[0][1]
    for i in range(n):
        if min >= li[i][1]:
            count += 1
            min = li[i][1]
    
    print(count)