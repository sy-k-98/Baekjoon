def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())

for i in range(n):
    num = list(map(int, input().split()))
    sum = 0

    for j in range(1, len(num)):
        for k in range(j+1, len(num)):
            sum += gcd(num[j], num[k])

    print(sum)
