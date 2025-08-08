from collections import deque

q = deque()
for _ in range(int(input())):
    cmd = input()
    if cmd == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        push, x = cmd.split()
        q.append(x)