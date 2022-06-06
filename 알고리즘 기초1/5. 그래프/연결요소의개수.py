import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)