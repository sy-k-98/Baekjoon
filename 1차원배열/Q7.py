n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    cnt = 0
    for score in num[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/num[0] *100
    print(f'{rate:.3f}%')