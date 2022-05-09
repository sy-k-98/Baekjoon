def count_num(n, k):
    cnt = 0
    while n != 0:
        n //= k
        cnt += n
    return cnt


n, m = map(int, input().split())

five_cnt = count_num(n, 5) - count_num(m, 5) - count_num(n - m, 5)
two_cnt = count_num(n, 2) - count_num(m, 2) - count_num(n - m, 2)

result = min(five_cnt, two_cnt)
print(result)