n = int(input())
num = list(map(int, input().split()))
answer = 0
for x in num:
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    if cnt == 2:
        answer += 1

print(answer)