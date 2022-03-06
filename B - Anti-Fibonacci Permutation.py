# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w

for _ in range(int(input())):
    n = int(input())
    ans = [i for i in range(n, 0, -1)]
    print(*ans)
    i = n - 1
    while (i > 0):
        ans[i], ans[i - 1] = ans[i - 1], ans[i]
        print(*ans)
        i -= 1