import sys
input= sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=[]
    for _ in range(n):
        for i in range(n-1):
            if a[i] >a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                res +=[(1,i +1)]
    for _ in range(n):
        for i in range(n-1):
            if b[i] >b[i+1]:
                b[i],b[i+1]=b[i+1],b[i]
                res +=[(2,i+1)]
    for i in range(n):
        if a[i] > b[i]:
            res +=[(3,i+1)]
    print(len(res))
    [print(*x) for x in res]