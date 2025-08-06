stick = list(map(int, input().split()))

stick.sort()
if stick[0] == stick[1] and stick[1] == stick[2]:
    print(2)
elif stick[0] ** 2 + stick[1] ** 2 == stick[2] ** 2:
    print(1)
else:
    print(0)