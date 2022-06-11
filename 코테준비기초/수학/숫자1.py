while True:
    try:
        n = int(input())
    except:
        break

    num = '1'
    cnt = 1
    while True:
        if int(num * cnt) % n == 0:
            print(cnt)
            break
        cnt += 1
