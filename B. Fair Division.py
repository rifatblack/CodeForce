import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')



for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = l.count(1)
    y = l.count(2)
    if (x%2==0 and (y%2==0 or x>=2)):
        print("YES")
    else:
        print("NO")