x = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
n = ''.join(reversed(n))
b = int(b)

answer = 0

for i in range(len(n) - 1, -1, -1):
    sum = x.index(n[i]) * (b ** i)
    answer += sum

print(answer)

