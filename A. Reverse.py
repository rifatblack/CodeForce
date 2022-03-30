# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')




for x in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    if a==1:
        print(b[0])
        continue
    else:
        c = sorted(b)
        for i in range(a-1):
            if b[i] == c[i]:
                continue
            else:
                tem = b.index(min(b[i+1:]))
                temp = b[i:tem+1]
                temp = temp[::-1]
                b = b[0:i] + temp + b[tem+1:]
                break
        for i in range(len(b)):
            print(b[i],end="")
            if i != len(b)-1:
                print(" ",end="")
        print()