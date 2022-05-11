num = []
while True:
    num = list(map(int, input().split()))
    if num.count(0) == 3:
        break
    num.sort()
    if num[2] ** 2 == num[0] ** 2 + num[1] ** 2:
        print("right")

    else:
        print("wrong")


