from collections import deque

for _ in range(int(input())):
    p = list(input())
    n = int(input())
    num = input()
    is_reversed = False
    flag = True
    
    if num == '[]':
        numbers = deque()
    else:
        numbers = deque(map(int, num[1:-1].split(',')))

    for i in p:
        if i == 'R':
            is_reversed = not is_reversed
        elif i == 'D':
            if not numbers:
                print('error')
                flag = False
                break
            if is_reversed:
                numbers.pop()
            else:
                numbers.popleft()
    
    if flag:
        if is_reversed:
            numbers.reverse()
        print(f"[{','.join(map(str, numbers))}]")