# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def fun(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append([a[i], i])

    b.sort()
    ans = 1
    pos = b[0][1]
    for i in range(1, n):
        if (b[i][1] != pos + 1):
            ans += 1
        pos = b[i][1]
    print(ans)
    if ans <= k:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    value = int(input())
    for t in range(value):
        fun(t)




