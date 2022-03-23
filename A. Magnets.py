# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n=int(input())
l=""
for i in range(0,n):
    a=input()
    l=l+a
p=l.count("00")
q=l.count("11")
print(int(p+q+1))