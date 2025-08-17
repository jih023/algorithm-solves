from collections import defaultdict

n = int(input())

adj = defaultdict(list)

for i in range(n-1):
    c, p = input().split()
    adj[p].append(c)

def dfs(node, ans):
    if node == ans:
        return True

    for i in adj[node]:
        if dfs(i, ans):
            return True
        
    return False

c1, c2 = input().split()

if dfs(c1, c2) or dfs(c2, c1):
    print(1)
else:
    print(0)