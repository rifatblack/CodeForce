# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input())
arr = [int(i) for i in input().split()]
arr1 = [0] * n
for i in arr:
    arr1[i - 1] = arr.index(i) + 1
print(*arr1)
