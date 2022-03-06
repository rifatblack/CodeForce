# import sys
# sys.stdin = open('input2.txt', 'r')
# sys.stdout = open('output.txt', 'w')

for i in range(int(input())):
    A = int(input())
    B = list(input().split())
    if B.count('1') == A:
        print(0)
    else:
        for j in range((len(B))-1,-1,-1):
            if B[j] == "0":
                break
        for i in range(A):
            if B[i]=="0":
                break
        print((j+1)-(i-1))