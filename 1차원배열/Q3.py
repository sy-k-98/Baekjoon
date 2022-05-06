a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)
cnt = [0] * 10

for i in range(len(num)):
    cnt[int(num[i])] += 1

for i in range(len(cnt)):
    print(cnt[i])

