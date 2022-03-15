# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input())
a = list(map(int, input().split()))
s_me = 0
s_ost = sum(a)
count = 0
while s_me <= s_ost:
    max_a = max(a)
    s_me += max_a
    a.remove(max_a)
    s_ost = sum(a)
    count += 1
print(count)