import sys

m = int(input())
s = set()

for _ in range(m):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()

    else:
        p, x = tmp[0], int(tmp[1])

        if p == "add":
            s.add(x)
        elif p == "remove":
            s.discard(x)
        elif p == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif p == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)