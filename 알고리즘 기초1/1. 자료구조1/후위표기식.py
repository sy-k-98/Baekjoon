import sys
input = sys.stdin.readline

x = list(input())
stack = []
answer = []

for i in x:
    if i.isalpha():
        answer.append(i)
    else:
        if i == '(':
            stack.append(i)

        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer.append(stack.pop())
            stack.append(i)

        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.append(i)

        elif i == ')':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.pop()
while stack:
    answer.append(stack.pop())

for a in answer:
    print(a, end="")