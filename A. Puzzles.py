
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def main():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    diff = s[-1] - s[0]
    for i in range(m - n + 1):
        if diff > s[i + n - 1] - s[i]:
            diff = s[i + n - 1] - s[i]
    print(diff)


if __name__ == '__main__':
    main()