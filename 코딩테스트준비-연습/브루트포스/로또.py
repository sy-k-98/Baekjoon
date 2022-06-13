from itertools import combinations

while True:
    test = list(map(int, input().split()))
    n = test[0]
    if n == 0:
        break
    answer = combinations(test[1:], 6)

    for x in answer:
        print(*x)
    print()


