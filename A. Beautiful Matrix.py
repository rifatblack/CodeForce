
# rows = 5
# cols= 5
# matrix = []
#
# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#     for j in range(cols):
#         if matrix[i][j] == 1:
#             MinimumMoves = abs(i + 3) - abs(j + 3)
#             print(abs(MinimumMoves))
#             exit()

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
d=[int(x) for x in input().split()]
e=[int(x) for x in input().split()]

if sum(a)!=0:
    x,y=1,a.index(1)+1
elif sum(b)!=0:
    x,y=2,b.index(1)+1
elif sum(c)!=0:
    x,y=3,c.index(1)+1
elif sum(d)!=0:
    x,y=4,d.index(1)+1
else:
    x,y=5,e.index(1)+1

r,c=3,3
print(abs(x-r)+abs(c-y))



