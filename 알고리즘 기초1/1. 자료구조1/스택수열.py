import sys
input = sys.stdin.readline

n = int(input())
stack = []
op = []
cnt = 1
tmp = True
for _ in range(n):

    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')

    else:
        tmp = False
        break

if tmp == False:
    print("NO")

else:
    for i in op:
        print(i)

