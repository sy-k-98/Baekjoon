from collections import deque
import sys
input = sys.stdin.readline

start = 1 # 시작점
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
children = [set() for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
test_case = list(map(int, input().split()))

# 6. BFS
queue = deque()
queue.append(start)
visited[start] = 0
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            children[x].add(i)
            queue.append(i)


next_index = 1
for i in test_case:
    if next_index == N:
        break
    c_length = len(children[i])
    c1 = set(test_case[next_index : next_index+c_length])
    c2 = children[i]
    if c1 != c2:
        print(0)
        exit()
    next_index += c_length
print(1)