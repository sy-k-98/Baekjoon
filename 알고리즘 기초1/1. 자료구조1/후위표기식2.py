import sys
input = sys.stdin.readline

n = int(input())
x = list(input().strip())
num = [0] * n

for i in range(n):
    num[i] = int(input())

stack = []

for i in x:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i) - ord('A')])
    else:
        s2 = stack.pop()
        s1 = stack.pop()

        if i == '+':
            stack.append(s1 + s2)
        elif i == '-':
            stack.append(s1 - s2)
        elif i == '*':
            stack.append(s1 * s2)
        elif i == '/':
            stack.append(s1 / s2)

print('%.2f' %stack[0])