num = 1000001
prime = [True] * num
for i in range(2, int((num-1)**0.5) + 1):
    if prime[i]:
        for j in range(i + i, num, i):
            prime[j] = False


t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0

    for i in range(2, int(n/2) + 1):
        if prime[i] and prime[n - i]:
            cnt += 1

    print(cnt)
