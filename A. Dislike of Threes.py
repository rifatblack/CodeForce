# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

t = int(input())
s = []
for i in range(2000):
    if (i % 3 != 0 and i % 10 != 3):
        s.append(i)
while (t != 0):
    k = int(input())
    print(s[k - 1])
    t = t - 1
