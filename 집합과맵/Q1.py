def binary_search(a, num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if a[mid] == num :
            return 1
        elif a[mid] > num :
            r = mid - 1
        else:
            l = mid + 1
    return 0


n = int(input())
have = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

have.sort()
for i in num:
    print(binary_search(have, i), end=" ")