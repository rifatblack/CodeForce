# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

t = int(input())

for _ in range(t):
    v = int(input())
    arr = list(map(int, input().split()))

    ut = nam = -1
    for j, i in enumerate(arr):
        if (i == 0):
            ut = j
    ans = []
    if (ut == -1):
        ans.append(v + 1)
    for i in range(v):
        ans.append(i + 1)
        if (ut == i):
            ans.append(v + 1)
    ans2 = [str(i) for i in ans]
    print(" ".join(ans2))