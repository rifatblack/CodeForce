# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


x = int(input(""))
ch = x
print(x)
for i in range((ch // 2), 0, -1):
    if ch % i == 0:
        print(i)
        ch = i
