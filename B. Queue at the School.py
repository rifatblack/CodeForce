# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


t=int(input()[2:])
s=input()
while t:
    s=s.replace('BG','GB')
    t-=1
print(s)