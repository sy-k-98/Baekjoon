import sys
input = sys.stdin.readline

MAX = 1000000

# 에라토스테네톤의 체
num = [True] * (MAX + 1)
for i in range(2, int(MAX ** 0.5) + 1):
    if num[i]:
        for j in range(i + i, MAX + 1, i):
            num[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    flag = 0
    for i in range(3, MAX + 1):
        if num[i] and num[n - i]:
            print(str(n) + " = " + str(i) + " + " + str(n - i))
            flag = 1
            break

    if flag == 0:
        print("Goldbach's conjecture is wrong.")
