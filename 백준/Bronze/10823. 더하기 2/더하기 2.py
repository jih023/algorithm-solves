import sys
s = sys.stdin.read()
s = s.replace('\n', '')

result = 0
a = ''
for i in s:
    if i == ',':
        result += int(a)
        a = ''
    else:
        a += i

result += int(a)
print(result)