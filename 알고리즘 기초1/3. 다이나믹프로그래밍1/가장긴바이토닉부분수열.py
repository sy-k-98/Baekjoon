n = int(input())
b = list(map(int, input().split()))

up = [1] * n
down = [1] * n

for i in range(n):
    for j in range(i):
        if b[i] > b[j]:
            up[i] = max(up[i], up[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if b[i] > b[j]:
            down[i] = max(down[i], down[j] + 1)

result = [0] * n
for i in range(n):
    result[i] = up[i] + down[i] -1

print(max(result))
