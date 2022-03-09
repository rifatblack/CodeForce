# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


first_word = input()
Second_word = input()

txt = first_word [::-1]
if txt == Second_word:
    print("YES")

else:
    print("NO")
