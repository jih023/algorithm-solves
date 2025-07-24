from collections import deque

n, k = map(int, input().split())
number = list(map(int, input()))

stack = deque([])

for i in range(n):
    if stack and (number[i] > stack[-1]):
        while stack and k:
            if number[i] > stack[-1]:
                stack.pop()
                k -= 1
            else:
                break
    
    stack.append(number[i])

if k:
    print("".join(map(str, list(stack)[:-k])))
else:
    print("".join(map(str, list(stack))))