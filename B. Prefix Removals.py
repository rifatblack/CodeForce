# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


from collections import defaultdict


def h():
    return 0


t = int(input())
for _ in range(t):
    s = list(input())
    d = defaultdict(h)
    for i in range(len(s)):
        d[s[i]] += 1
    i = 0
    while 1:
        if i == len(s) - 1:
            print("".join(s[i:]))
            break
        if d[s[i]] > 1:
            d[s[i]] -= 1
            i += 1
        else:
            print("".join(s[i:]))
            break
