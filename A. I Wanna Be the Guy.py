# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def iWannaBeTheGuy():
    n = int(input())
    count = 0
    values1 = (input().split())
    values2 = (input().split())
    values1 = set(values1[1:])
    values2 = set(values2[1:])
    values = values1.union(values2)
    for i in range(1, len(values) + 1):
        if str(i) in values:
            count += 1
    if count == n:
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')
    # print(values1)


iWannaBeTheGuy()