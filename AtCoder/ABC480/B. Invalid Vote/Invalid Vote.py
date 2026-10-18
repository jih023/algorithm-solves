n, m = map(int, input().split())
s = dict((input(), 0) for i in range(n))

for _ in range(m):
    name = input()
    if name in s:
        s[name] += 1
    else:
        cnt = 0
        for i in range(len(name)):
            for alphabet in 'abcdefghijklmnopqrstuvwxyz':
                new_name = name[:i] + alphabet + name[i+1:]
                if new_name in s:
                    cnt += 1
                    ans_name = new_name

        if cnt == 1:
            s[ans_name] += 1

print('\n'.join(str(s[name]) for name in s))