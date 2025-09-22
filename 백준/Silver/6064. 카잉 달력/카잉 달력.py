def gcd(m, n):
    while n != 0:
        t = m % n
        m, n = n, t
    return abs(m)

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    lcm = (m * n) // gcd(m, n)
    result = -1

    nx, ny = x, x 
    cnt = x

    while cnt <= lcm:
        if ny % n == 0:
            cy = n
        else:
            cy = ny % n

        if cy == y:
            result = cnt
            break

        ny += m  
        cnt += m
    
    print(result)