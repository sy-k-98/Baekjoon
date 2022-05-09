from math import gcd

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))
num.sort()

tmp = [num[i] - num[i-1] for i in range(1, n)]
a = tmp[0]

for i in range(1, n-1):
    a = gcd(a, tmp[i])

result = []
for i in range(1, int(pow(a, 1/2)) + 1): # a의 제곱근까지
    if a % i == 0:
        if i ** 2 == a:
            result.append(i)
        else:
            result += [i, a // i]

result.remove(1)
result.sort()

for i in result:
    print(i, end=" ")


