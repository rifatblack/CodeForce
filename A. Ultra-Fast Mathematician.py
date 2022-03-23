# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

a = input()
b = input()
l = []
for i in range(len(a)):
    if (a[i] != b[i]):
        l.append("1")
        print(l[i], end="")
    else:
        l.append("0")
        print(l[i], end="")
