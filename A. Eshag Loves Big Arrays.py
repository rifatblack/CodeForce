for t in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    print(n-lst.count(min(lst)))