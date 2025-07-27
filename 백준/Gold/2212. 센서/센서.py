import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))

if k >= n:
    print(0)
    exit()

sensors.sort()

diff = [sensors[i+1] - sensors[i] for i in range(n - 1)]

diff.sort(reverse=True)

print(sum(diff[k-1:]))