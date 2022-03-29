# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())

h = []
g = []

for _ in range(n):
    hi, ai = map(int, input().split())
    h.append(hi)
    g.append(ai)

count = 0
for i in range(n):
    for j in range(n):
        if h[i] == g[j]:
            count += 1

print(count)