x, y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num = set(A) ^ set(B)

print(len(num))