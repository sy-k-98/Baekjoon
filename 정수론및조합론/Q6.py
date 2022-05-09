from math import gcd

n = int(input())
num = list(map(int, input().split()))

num_gcd = []
ring = num[0]
for i in range(1, n):
    num_gcd.append(gcd(ring, num[i]))

for i in range(n - 1):
    print(str(ring//num_gcd[i])+"/"+str(num[i+1]//num_gcd[i]))