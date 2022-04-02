# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


word1 = input()
word2 = input()
word3 = list(input())
new_word = list(word1 + word2)
new_word.sort()
word3.sort()
if new_word == word3:
    print("YES")
else:
    print("NO")