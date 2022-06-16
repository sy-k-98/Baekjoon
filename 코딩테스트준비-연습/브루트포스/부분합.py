n, s = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
m = 100001
t = 0

while True:
    if t >= s:
        m = min(m, right - left)
        t -= a[left]
        left += 1

    elif right == n:
        break

    else:
        t += a[right]
        right += 1

if m == 100001:
    print(0)
else:
    print(m)