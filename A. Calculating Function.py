# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n=int(input())
if n%2==0:
    print(n//2)
else:
    print((n//2)-n)