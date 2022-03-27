# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


s = input()
st = set()
for i in s:
    if i >= 'a' and i <= 'z':
        st.add(i)

print(len(st))