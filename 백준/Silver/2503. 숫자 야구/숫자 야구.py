n = int(input())

question = []
for _ in range(n):
    num, strike, ball = input().split()
    question.append([num, int(strike), int(ball)])

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
result = 0
for a in number:
    for b in number:
        if b == a:
            continue
        for c in number:
            if c == a or c == b:
                continue

            flag = 0
            for num, strike, ball in question:
                s_check = 0
                b_check = 0
                if num[0] == a:
                    s_check += 1
                elif num[1] == a or num[2] == a:
                    b_check += 1
                if num[1] == b:
                    s_check += 1
                elif num[0] == b or num[2] == b:
                    b_check += 1
                if num[2] == c:
                    s_check += 1
                elif num[0] == c or num[1] == c:
                    b_check += 1

                if s_check != strike or b_check != ball:
                    flag = 1
                    break 
            
            if not flag:
                result += 1

print(result)