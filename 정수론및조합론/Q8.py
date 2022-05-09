li = [[0 for i in range(1001)] for j in range(1001)]
li[0][0] = li[1][0] = li[1][1] = 1
for i in range(2, 1001):
    for j in range(i+1):
        if j == 0 or i == j:
            li[i][j] = 1
        else:
            li[i][j] = li[i-1][j-1] + li[i-1][j]
n1, n2 = map(int, input().split())
print(li[n1][n2] % 10007)