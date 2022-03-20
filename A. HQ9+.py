# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
s = input()
f=1
for i in s:
    if i == "H":
        f=0
        print("YES")
        break
    elif i == "Q":
        f=0
        print("YES")
        break
    elif i == "9":
        f=0
        print("YES")
        break
if f:
    print("NO")