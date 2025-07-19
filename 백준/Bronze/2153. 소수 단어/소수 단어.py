def is_prime(n):
    if n == 1:
        return True 
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

word = input()

total = 0
for i in word:
    if 'a' <= i <= 'z':
        total += ord(i) - ord('a') + 1
    elif 'A' <= i <= 'Z':
        total += ord(i) - ord('A') + 27

if is_prime(total):
    print("It is a prime word.")
else:
    print("It is not a prime word.")