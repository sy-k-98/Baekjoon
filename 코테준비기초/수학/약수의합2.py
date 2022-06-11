# def divisor(n):
#     d = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             d.append(i)
#     return sum(d)
#
#
# n = int(input())
# answer = 0
# for i in range(1, n + 1):
#     answer += divisor(i)
#
# print(answer)

n = int(input())
answer = 0
for i in range(1, n + 1):
    answer += (n // i) * i  # 약수의 합 = i를 약수로 가지고 있는 수  * 개수

print(answer)