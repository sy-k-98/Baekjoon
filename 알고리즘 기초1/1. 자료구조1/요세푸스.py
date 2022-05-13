import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]
result = []
num = 0

for i in range(n):
    num += (k - 1)
    if num >= len(nums):
        num %= len(nums)

    result.append(str(nums[num]))
    nums.pop(num)

print("<", ', '.join(result), ">", sep="")
