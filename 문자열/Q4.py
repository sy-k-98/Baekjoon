T = int(input())

for _ in range(T):
    n, s = input().split()

    for i in s:
        print(i * int(n), end='')

    print()