# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def spiral1(t):
    n, k = map(int, input().split())
    a = [[1, 2, 9, 10, 25],
         [4, 3, 8, 11, 24],
         [5, 6, 7, 12, 23],
         [16, 15, 14, 13,22],
         [17, 18, 19, 20,21]]
    n1=n-1
    n2=k-1

    print(a[n1][n2])


if __name__ == '__main__':
    input1= int(input())
    for x in range(input1):
        spiral1(x)