n = int(input())
for i in range(n):
    flag = True
    st = list(input())
    ho = []
    for j in st:
        if j == '(':
            ho.append(1)
        else:
            if len(ho) == 0:
                flag = False
                break
            else:
                ho.pop()

    if len(ho) >= 1:
        flag = False

    if flag:
        print('YES')
    else:
        print('NO')

