# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = list(map(int,input().split()))
count = 0
input_count= []

for x in range(4):
    if n[x] in input_count:
        count +=1
    else:
        input_count.append(n[x])

print(count)