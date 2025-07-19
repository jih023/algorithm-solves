n, k = map(int, input().split())
dolls = list(map(int, input().split()))

lion_indices = [i for i, val in enumerate(dolls) if val == 1]

if len(lion_indices) < k:
    print(-1)
else:
    min_length = n + 1

    for i in range(len(lion_indices) - k + 1):
        start = lion_indices[i]
        end = lion_indices[i + k - 1]
        length = end - start + 1
        min_length = min(min_length, length)
    
    print(min_length)