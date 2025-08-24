A, B = input().split()
lenA = len(A)
lenB = len(B)

min_diff = float('inf')

for i in range(lenB - lenA + 1):
    diff = 0
    for j in range(lenA):
        if A[j] != B[i+j]:
            diff += 1
    min_diff = min(min_diff, diff)

print(min_diff)