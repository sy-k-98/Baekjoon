n = int(input())

for _ in range(n):
    quiz = list(input())
    cnt = 0
    sum = 0
    for i in quiz:
        if i == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)