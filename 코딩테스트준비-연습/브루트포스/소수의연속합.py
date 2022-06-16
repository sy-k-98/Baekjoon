import math

n = int(input())
prime = [False, False] + [True] * (n - 1)
prime_num = []
for i in range(2, n + 1):
    if prime[i]:
        prime_num.append(i)
        for j in range(2 * i, n + 1, i):
            prime[j] = False

answer = 0
left = 0
right = 0

while right <= len(prime_num):
    s = sum(prime_num[left : right])
    if s == n:
        answer += 1
        right += 1
    elif s < n:
        right += 1
    else:
        left += 1

print(answer)
