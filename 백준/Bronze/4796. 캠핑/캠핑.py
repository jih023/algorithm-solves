idx = 0

while (1):
    l, p, v = map(int, input().split())
    
    if (l == 0 and p == 0 and v == 0):
        break

    idx += 1
    p_num = v // p
    v -= p_num * p

    if v >= l:
        print('Case ', idx, ': ', (p_num + 1) * l, sep="")
    else:
        print('Case ', idx, ': ', p_num * l + v, sep="")