from collections import deque

n, m, fuel = map(int, input().split())
b_map = [[0] * (n + 1)]  

for _ in range(n):
    row = list(map(int, input().split()))
    b_map.append([0] + [(-1 if x == 1 else x) for x in row])

r, c = map(int, input().split())

passenger = []
for i in range(m):
    s_r, s_c, e_r, e_c = map(int, input().split())
    passenger.append((e_r, e_c))
    b_map[s_r][s_c] = i + 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

find_path = False
for _ in range(m):
    q1 = deque()
    q2 = deque()
    visited1 = [[0 for _ in range(21)] for _ in range(21)]
    visited2 = [[0 for _ in range(21)] for _ in range(21)]

    find_path = False
    used_fuel1 = 401

    if b_map[r][c] >= 1:
        find_path = True
        customer_num = b_map[r][c]
        used_fuel1 = 0
    else:
        q1.append(((r, c), 0))
        visited1[r][c] = 1
    
    while q1:
        pos, depth = q1.popleft()

        if (fuel <= depth or depth >= used_fuel1):
            break
            
        for i in range(4):
            nr, nc = pos[0] + dr[i], pos[1] + dc[i]

            if (1 <= nr and nr <= n and 1 <= nc and nc <= n and b_map[nr][nc] != -1 and not visited1[nr][nc]):
                if 1 <= b_map[nr][nc]:
                    if not find_path:
                        find_path = True
                        customer_num = b_map[nr][nc]
                        r = nr
                        c = nc
                        
                        used_fuel1 = depth + 1
                    else:
                        if nr < r:
                            customer_num = b_map[nr][nc]
                            r = nr
                            c = nc
                        elif nr == r:
                            if nc < c:
                                customer_num = b_map[nr][nc]
                                r = nr
                                c = nc
                else:
                    q1.append(((nr, nc), depth + 1))
                    visited1[nr][nc] = True
        
    if not find_path:
        break
    b_map[r][c] = 0
    fuel -= used_fuel1

    find_path = False
    used_fuel2 = 401

    q2.append(((r, c), 0))
    visited2[r][c] = True

    while q2:
        pos, depth = q2.popleft()

        if (fuel <= depth or find_path):
            break
            
        for i in range(4):
            nr, nc = pos[0] + dr[i], pos[1] + dc[i]

            if (1 <= nr and nr <= n and 1 <= nc and nc <= n and b_map[nr][nc] != -1 and not visited2[nr][nc]):
                destination_r, destination_c = passenger[customer_num - 1]
                if nr == destination_r and nc == destination_c:
                    find_path = True
                    r = nr
                    c = nc
                    
                    used_fuel2 = depth + 1
                else:
                    q2.append(((nr, nc), depth + 1))
                    visited2[nr][nc] = True
    
    if not find_path:
        break
    fuel -= used_fuel2
    fuel += used_fuel2 * 2

if not find_path:
    print(-1)
else:
    print(fuel)