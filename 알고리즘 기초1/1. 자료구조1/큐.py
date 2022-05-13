import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = input().strip().split()

    if x[0] == 'push':
        q.append(x[1])

    elif x[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(q))

    elif x[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif x[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif x[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])