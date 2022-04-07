# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())
a = str(input())
a = a.lower()
sum = 0
for i in range(97, 123):
    p = 0
    for j in a:
        if ord(j) == i:
            p = 1
    sum += p
if sum == 26:
    print("YES")
else:
    print("NO")