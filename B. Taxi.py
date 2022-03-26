# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())
s = list(map(int,input().split()))
a = s.count(1)
b = s.count(2)
c = s.count(3)
d = s.count(4)
if c>=a:
    print(d+c+(b+1)//2)
else:
    if b%2==0:
        print(d+c+b//2+(a-c+3)//4)
    else:
        print(d+c+b//2+(a-c+5)//4)











