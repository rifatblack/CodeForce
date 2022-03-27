# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def main():
    s = input().lower()
    c = input().lower()
    a = 0
    for i in s:
        a += 1
        if i == c:
            if a % 2 == 1:
                return 'Yes'
    return 'No'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(main())