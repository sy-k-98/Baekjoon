import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
no = list(map(int, input().split()))

cnt = abs(100 - n)

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        if int(num[j]) in no:
            break

        elif j == len(num) - 1:
            cnt = min(cnt, abs(int(num) - n) + len(num))

print(cnt)
