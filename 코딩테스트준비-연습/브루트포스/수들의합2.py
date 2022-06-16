n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= n and left <= right:

    num = a[left:right]
    total = sum(num)

    if total == m:
        cnt += 1
        right += 1

    elif total < m:
        right += 1

    else:
        left += 1

print(cnt)