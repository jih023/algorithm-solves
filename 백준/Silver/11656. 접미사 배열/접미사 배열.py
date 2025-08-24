S = input().strip() 

suffixes = [S[i:] for i in range(len(S))]

suffixes.sort()

for suf in suffixes:
    print(suf)