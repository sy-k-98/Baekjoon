def DFS():
    if len(result) == m:
        print(*result)
        return

    for i in range(n):
        result.append(num[i])
        DFS()
        result.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []

DFS()