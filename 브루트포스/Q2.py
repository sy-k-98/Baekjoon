n = int(input())

for i in range(n):
    a = sum(map(int, str(i)))
    b = a + i
    if b == n:
        print(i)
        break
else:
    print(0)