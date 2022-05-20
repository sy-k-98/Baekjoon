a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))
num.reverse()

ten = 0
for i in range(m):
    ten += num[i] * (a ** i)

answer = []
while ten != 0:
    answer.append(str(ten % b))
    ten = ten // b

print(*answer[::-1])