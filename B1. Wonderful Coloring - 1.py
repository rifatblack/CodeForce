# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

for _ in range(int(input())):
    s=str(input())
    l=set(s)
    c=0
    for i in l:
        if s.count(i)>1:
            c+=2
        else:
            c+=1
    print(c//2)