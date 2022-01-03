# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def f(l):
    odd = []
    even = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if abs(len(odd) - len(even)) > 1:
        return -1
    ans = 0
    if len(odd) > len(even):
        for i in range(len(odd)):
            ans += abs(odd[i] - (2 * i))
        return ans
    if len(odd) < len(even):
        for i in range(len(even)):
            ans += abs(even[i] - (2 * i))
        return ans
    ans2 = 0
    for i in range(len(odd)):
        ans += abs(odd[i] - 2 * i)
    for i in range(len(odd)):
        ans2 += abs(odd[i] - (2 * i + 1))
    return min(ans, ans2)


n = int(input())
for i in range(n):
    a = input()
    lis = input()
    lis = lis.split()
    for i in range(len(lis)):
        lis[i] = int(lis[i])
    print(f(lis))

