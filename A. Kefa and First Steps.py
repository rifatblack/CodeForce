# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input())
spisok = list(map(int,input().split()))
ans = 0
max = 0
for i in range(n-1):
    if spisok[i]<=spisok[i+1]:
        ans+=1
    else:
        ans = 0
    if ans > max:
        max = ans
print(max+1)


