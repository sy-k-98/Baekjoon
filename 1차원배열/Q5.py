n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)

for i in range(n):
    arr[i] = arr[i] / max_value * 100

print(sum(arr) / len(arr))