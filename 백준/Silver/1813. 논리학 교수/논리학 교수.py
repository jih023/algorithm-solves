n = int(input())
num = list(map(int, input().split()))

true_list = [0] * 51

for i in num:
    true_list[i] += 1

impossible = 1
for i in range(50, -1, -1):
    if true_list[i] == i:
        impossible = 0
        print(i)
        break

if impossible:
    print(-1)