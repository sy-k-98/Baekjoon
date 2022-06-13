n = int(input())
word = []
for _ in range(n):
    word.append(input())

num = {}

for w in word:
    l = len(w) - 1
    for x in w:
        if x not in num:
            num[x] = pow(10, l)
        else:
            num[x] += pow(10, l)
        l -= 1

num = sorted(num.values(), reverse=True)

answer = 0
m = 9

for i in num:
    answer += i * m
    m -= 1

print(answer)