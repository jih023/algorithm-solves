def calculate_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a // b

def priority(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    else:
        return 0
    
# 0 - 숫자, 1 - 여는 괄호, 2 - 연산기호, 3 - 닫는 괄호
def validate(expr):
    if expr[0] in '+-/*)':
        return False
    
    bal = 0

    if expr[0].isdigit():
        pre = 0
    elif expr[0] == '(':
        pre = 1
        bal += 1
    else:
        return False
    
    for i in range(1, len(expr)):
        c = expr[i]

        if c.isdigit():
            if pre == 3:
                return False
            pre = 0
        
        elif c == '(':
            if pre == 0 or pre == 3:
                return False
            bal += 1
            pre = 1
        
        elif c == ')':
            if pre == 1 or pre == 2 or bal == 0:
                return False
            bal -= 1
            pre = 3
        
        elif c in '+-/*':
            if pre == 1 or pre == 2:
                return False
            pre = 2
        
        else:
            return False
    
    if pre == 2 or bal != 0:
        return False
    
    return True

expr = input()

nums = []
ops = []
flag = 1
idx = 0

if validate(expr):
    while idx < len(expr):
        i = expr[idx]

        if i == '(':
            ops.append(i)

        elif i == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                b = nums.pop()
                a = nums.pop()
                if b == 0 and op == '/':
                    flag = 0
                    break
                nums.append(calculate_op(a, b, op))
            ops.pop()

        elif i.isdigit():
            num = 0
            while idx < len(expr) and expr[idx].isdigit():
                num = num * 10 + int(expr[idx])
                idx += 1
            nums.append(num)
            continue

        else:
            while ops and ops[-1] != '(' and priority(ops[-1]) >= priority(i):
                op = ops.pop()
                b = nums.pop()
                a = nums.pop()
                if b == 0 and op == '/':
                    flag = 0
                    break
                nums.append(calculate_op(a, b, op))
            ops.append(i)
        idx += 1

    while ops and nums:
        op = ops.pop()
        b = nums.pop()
        a = nums.pop()
        if b == 0 and op == '/':
            flag = 0
            break
        nums.append(calculate_op(a, b, op))
else:
    flag = 0

if flag and len(nums) == 1 and len(ops) == 0:
    print(nums[0])
else:
    print('ROCK')