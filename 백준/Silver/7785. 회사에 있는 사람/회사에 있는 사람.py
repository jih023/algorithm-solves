enter = []
for i in range(int(input())):
    name, action = input().split()
    
    if action == 'enter':
        enter.append(name)
    else:
        enter.remove(name)

enter.sort(reverse = True)
for i in enter:
    print(i)