m, n = map(int, input().split())

for x in range(m, n + 1):
    for i in range(2, int(x ** 0.5) + 1):  # 약수는 대칭이기 때문에 제곱근까지만 확인
        if x % i == 0:
            break
    else:
        print(x)
