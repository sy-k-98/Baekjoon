from collections import deque
import random

n = int(input())
tree = [[] for _ in range(n + 1)]

# 정점 번호, 간선 정보 - 정점번호, 거리, 마지막 입력 -1
for _ in range(n):
    node = list(map(int, input().split()))
    # 0번째 idx는 정점번호, 1 ~ len(node)의 길이-2 idx (정점번호, 거리, 정점번호, 거리) 순으로 데이터가 저장, 마지막 idx: -1
    for i in range(1, len(node) - 2, 2):
        cur_edge = node[0]
        edge, cost = node[i], node[i + 1] # 연결된 노드와 거리(정점번호, 거리)
        tree[cur_edge].append((edge, cost))


def bfs(start):
    visit = [-1] * (n + 1)
    q = deque()
    q.append(start)
    visit[start] = 0
    _max = [0, 0]

    while q:
        x = q.popleft()
        for e, d in tree[x]:
            if visit[e] == -1:
                visit[e] = visit[x] + d
                q.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e
    return _max


random_node = random.randrange(1, n+1)
distance, node = bfs(random_node)
distance, node = bfs(node)
print(distance)