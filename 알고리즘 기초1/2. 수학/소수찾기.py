n = int(input())
num = list(map(int, input().split()))

cnt = 0

for i in num:
    c = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                c += 1

        if c == 0:
            cnt += 1

print(cnt)


