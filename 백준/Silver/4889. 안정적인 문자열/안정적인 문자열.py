cnt = 1
while True:
    string = input()
    if '-' in string:
        break

    stack = []
    result = 0
    for i in string:
        if i == '{':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                result += 1
                stack.append('{')
    
    result += len(stack) // 2
    print(cnt, '. ', result, sep="")
    cnt += 1