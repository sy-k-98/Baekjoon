def DFS():
    if len(result) == m:
        print(*result)
        return

    flag = 0
    for i in range(n):
        if flag == num[i]:
            continue

        result.append(num[i])
        flag = num[i]
        DFS()
        result.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []


DFS()