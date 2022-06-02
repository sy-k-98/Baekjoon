n = int(input())
s = []

def DFS():
    if len(s) == n:
        print(*s)
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            DFS()
            s.pop()

DFS()