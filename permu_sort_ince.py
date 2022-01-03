import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
x=3
y=5
z=0


def reverse(str, l, h):

    while (l < h) :
        str[l], str[h] = str[h], str[l]
        l += 1
        h -= 1

    return str

def findCeil(str, c, k, n):

    ans = -1
    val = c

    for i in range(k, n + 1):
        if str[i] > c and str[i] < val:
            val = str[i]
            ans = i

    return ans


def sortedPermutations(str):


    size = len(str)


    str = ''.join(sorted(str))


    isFinished = False

    while (not isFinished):


        print(str)


        for i in range(size - 2, -1, -1):
            if (str[i] < str[i + 1]):
                break


        if (i == -1):
            isFinished = True
        else:


            ceilIndex = findCeil(str, str[i], i + 1,
                                 size - 1)

            # Swap first and second characters
            str[i], str[ceilIndex] =  str[ceilIndex], str[i]


            str = reverse(str, i + 1, size - 1)



# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#
# from itertools import combinations
#
# n2=input()
#
# case_1=[]
# case_2=[]
#
#
# for i in range(len(n2)):
#     n = int(input())
#
#     first_case = list(map(int, input().split()))
#
#     first_case.insert(0,1)
#
#     comb = combinations(first_case,n)
#
#
#     for y in list(comb):
#         y1= sorted(y)
#         case_1.append(y)
#         case_2.append(y1)
#
#
# print(case_1)
# print(case_2)



# comb = combinations(case_1, n1)
#
# for y in list(comb):
#     print(y)