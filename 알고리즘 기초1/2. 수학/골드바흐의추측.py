import sys
input = sys.stdin.readline

num = 1000001
data = [True] * num
for i in range(2, int((num-1)**0.5) + 1):
    if data[i]:
        for j in range(i + i, num, i):
            data[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(3, len(data)):
        if data[i] and data[n - i] :
            print(str(n) + " = " + str(i) + " + " + str(n - i))
            cnt = 1
            break

    if cnt == 0:
        print("Goldbach's conjecture is wrong.")