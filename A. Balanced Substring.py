# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


t = int(input())
for case in range(t):
    n = int(input())
    s = input()
    a = -1
    b = -1
    for i in range(n-1):
        if(s[i]!=s[i+1]):
            a = i+1
            b = i+2
            break
    print(a, b)
