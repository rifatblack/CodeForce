# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n, k = map(int, input().split())
if k <= n-n//2:
    print(2*k-1)
else:
    k -= n-n//2
    print(2*k)