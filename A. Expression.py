# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

a=int(input())
b=int(input())
c=int(input())
print(max(a+b*c,a*(b+c),a*b*c,(a+b)*c,a+b+c))