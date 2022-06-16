from itertools import combinations

n, m = map(int, input().split())
num = list(map(int, input().split()))

# 주어진 숫자 n이 너무 커서 num을 절반으로 나눔
num1 = num[:len(num) // 2]
num2 = num[len(num) // 2:]
list_1 = []
list_2 = []

for i in range(0, len(num1) + 1):
    list_1 += list(sum(k) for k in combinations(num1, i))
    list_1.sort()

for i in range(0, len(num2) + 1):
    list_2 += list(sum(k) for k in combinations(num2, i))
    list_2.sort()

left = 0
right = len(list_2) - 1
cnt = 0
while left < len(list_1) and right >= 0:
    temp = list_1[left] + list_2[right]
    # list_1[left] + list_2[right] ==m 이라면 left-=1 right+=1
    if temp == m:
        temp1 = 1
        temp2 = 1
        left += 1
        right -= 1
        while left < len(list_1) and list_1[left] == list_1[left - 1]:
            temp1 += 1
            left += 1
        while right >= 0 and list_2[right] == list_2[right + 1]:
            temp2 += 1
            right -= 1
        cnt += temp1 * temp2
    elif temp < m:
        if left + 1 < len(list_1):
            left += 1
        else:
            break
    else:
        if right - 1 >= 0:
            right -= 1
        else:
            break
if m == 0:
    cnt -= 1
    
print(cnt)
