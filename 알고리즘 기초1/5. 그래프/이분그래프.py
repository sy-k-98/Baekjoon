import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        x = q.popleft()
        for i in matrix[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                q.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True


num = int(input())
for i in range(num):
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    flag = 1
    for _ in range(m):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)

    for i in range(1, n + 1):
        if visited[i] == 0:
            if not bfs(i):
                flag = -1
                break

    print('YES' if flag == 1 else 'NO')
