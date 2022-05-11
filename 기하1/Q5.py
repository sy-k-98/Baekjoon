k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

x = 0; x_index = 0
y = 0; y_index = 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if x < arr[i][1]:
            x = arr[i][1]
            x_index = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if y < arr[i][1]:
            y = arr[i][1]
            y_index = i

sub_x = abs(arr[(x_index - 1) % 6][1] - arr[(x_index + 1) % 6][1])
sub_y = abs(arr[(y_index - 1) % 6][1] - arr[(y_index + 1) % 6][1])

result = ((x * y) - (sub_x * sub_y)) * k
print(result)

