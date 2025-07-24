from collections import deque

front_space = deque(list(input()))
back_space = deque([])

for _ in range(int(input())):
    command = input()
    if command == 'L':
        if front_space:
            back_space.appendleft(front_space.pop())
    elif command == 'D':
        if back_space:
            front_space.append(back_space.popleft())
    elif command == 'B':
        if front_space:
            front_space.pop()
    else:
        p, n = command.split()
        front_space.append(n)

print("".join(list(front_space) + list(back_space)))