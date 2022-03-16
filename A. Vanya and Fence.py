# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

raw = input().split(" ")
n, h = map(int, raw)
arr = input().split(" ")
arr = [int(x) for x in arr]
ans = 0

for height in arr:
    if height > h:
        ans += 2
    else:
        ans += 1

print(ans)
