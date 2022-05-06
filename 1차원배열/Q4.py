arr = []
rest = []

for i in range(10):
    arr.append(int(input()))
    rest.append(arr[i] % 42)

print(len(set(rest)))