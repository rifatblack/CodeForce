
n,k = map(int,input().split())
score = list(map(int,input().split()))
temp = score[k-1]
count=0
for i in range(0,len(score)):
    if score[i]>=temp and score[i]>0:
        count +=1
print(count)