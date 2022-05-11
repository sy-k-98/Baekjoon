n, w, h = map(int, input().split())

for _ in range(n):
    i = int(input())
    if i <= (w**2 + h**2)**0.5:
        print("DA")
    else:
        print("NE")