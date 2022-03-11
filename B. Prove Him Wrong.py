# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

for _ in range(int(input())):
    n=int(input())
    p=[]
    if n>19:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            p.append(pow(3, i))
        print(*p)