import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 1-based

ans = [[0] * (N + 2) for _ in range(2)]
minus_cnt = [0] * (N + 2)

cnt = 0

for i in range(1, N + 1):
    a = arr[i]

    next_idx = a // M + 1 + i
    if a % M == 0:
        next_idx -= 1

    if next_idx <= N:
        minus_cnt[next_idx] += 1
        rem = (M - (a % M)) % M
        ans[0][next_idx] += rem
        ans[1][next_idx] -= rem

    ans[0][i] += a + ans[0][i - 1] - cnt * M
    ans[1][i] += cnt * M

    cnt -= minus_cnt[i]
    cnt += 1

for _ in range(Q):
    c, t = map(int, input().split())
    print(ans[c - 1][t])