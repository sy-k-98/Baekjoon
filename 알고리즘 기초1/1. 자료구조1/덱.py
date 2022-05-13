import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    tmp = input().strip().split()
    if tmp[0] == 'push_front':
        d.appendleft(tmp[1])

    elif tmp[0] == 'push_back':
        d.append(tmp[1])

    elif tmp[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())

    elif tmp[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif tmp[0] == 'size':
        print(len(d))

    elif tmp[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif tmp[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])

    elif tmp[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
