# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

t = int(input())
while t:
    n = int(input())
    s = input()
    s1 = ""
    j = n + 2
    s = list(s)
    for i in range(n):
        if s[i] != '?':
            j = i
            break
    if j < n:
        if s[j] == 'B':
            for k in range(1, j + 1):
                if k % 2 == 0:
                    s[j - k] = 'B'
                else:
                    s[j - k] = 'R'
        else:
            for k in range(1, j + 1):
                if k % 2 == 0:
                    s[j - k] = 'R'
                else:
                    s[j - k] = 'B'
        for k in range(j + 1, n):
            if s[k] == '?':
                if s[k - 1] == 'B':
                    s[k] = 'R'
                else:
                    s[k] = 'B'
    else:
        for i in range(n):
            if i % 2 == 0:
                s[i] = 'R'
            else:
                s[i] = 'B'
    print("".join(s))

    t -= 1