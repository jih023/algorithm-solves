for i in range(int(input())):
    sides = list(map(int, input().split()))
    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("Case #", i+1, ": YES", sep="")
    else:
        print("Case #", i+1, ": NO", sep="")