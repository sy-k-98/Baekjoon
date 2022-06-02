n = int(input())
num = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if num[i] < num[i-1]:
        x, y = i-1, i
        for j in range(n-1, 0, -1):
            if num[j] < num[x]:
                num[j], num[x] = num[x], num[j]
                num = num[:i] + sorted(num[i:], reverse=True)
                print(*num)
                exit(0)

print(-1)
