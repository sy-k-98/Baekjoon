n = int(input())
cnt = 0

m = n
while 1:
    a = m // 10
    b = m % 10
    c = a + b
    res = (b * 10) + (c % 10)
    cnt += 1
    m = res

    if res == n:
        print(cnt)
        break
