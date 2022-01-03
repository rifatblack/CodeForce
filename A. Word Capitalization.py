

word = input()

value=[]
for x in range(len(word)):
    if x == 0:
        value.append(word[x].upper())
    else:
        value.append(word[x])

Output="".join([c for c in value])

print(Output)
