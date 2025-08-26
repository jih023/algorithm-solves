n = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * n
for i in range(n):
    if not stack:
        stack.append(i)
    else:
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

print(" ".join(map(str, result)))