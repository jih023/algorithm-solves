s1, s2 = map(int, input().split())

sample = []
system = []
flag1 = 1
flag2 = 1

for _ in range(s1):
    a, b = map(int, input().split())
    if a != b:
        flag1 = 0

for _ in range(s2):
    a, b = map(int, input().split())
    if a != b:
        flag2 = 0

if not flag1:
    print('Wrong Answer')
elif not flag2:
    print('Why Wrong!!!')
else:
    print('Accepted')