m, s = map(int, input().split())
if s == 0:
    print('0 0\n' if m == 1 else '-1 -1\n')
    exit()

a = '9' * (s // 9)

if s % 9:
    a += f'{s % 9}'

if len(a) > m:
    print('-1 -1\n')
    exit()

max_ans = a


while len(a) < m:
    a = a[:-1] + f'{int(a[-1]) - 1}'
    while len(a) < (m - 1):
        a += '0'
    a += '1'

min_ans = a[::-1]


while len(max_ans) < m:
    max_ans += '0'

print(f'{min_ans} {max_ans}')