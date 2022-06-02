n = int(input())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

visited = [0] * n
result = 123456789
add = 0

def DFS(f, add, visited):
    global result
    if add > result:
        return
    if sum(visited) == n - 1:
        if city[f][0]:
            result = min(result, add + city[f][0])
        return
    for i in range(1, n):
        if city[f][i] and visited[i] == 0:
            visited[i] = 1
            DFS(i, add + city[f][i], visited)
            visited[i] = 0

for i in range(1, n):
    if city[0][i]:
        visited[i] = 1
        DFS(i, city[0][i], visited)
        visited[i] = 0

print(result)