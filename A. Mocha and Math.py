# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')





# for t in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     k = a[0]
#     for i in range(1, len(a)):
#         k &= a[i]
#     print(k)

for t in range(1):

    a = [2,3,3,3,54,22,100]
    k = a[0]
    for i in range(1, len(a)):
        k %= a[i]
    print(k)

