from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
visited = [False] * (N + 1)
answer = [0] * (N + 1)
Tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)


def DFS(Tree, root, visited):
    q = deque([root])
    visited[root] = True
    while q:
        x = q.popleft()
        for i in Tree[x]:
            if not visited[i]:
                answer[i] = x
                q.append(i)
                visited[i] = True


DFS(Tree, 1, visited)

for i in range(2, N + 1):
    print(answer[i])
