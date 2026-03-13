t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    c=[tuple(map(int,input().split())) for _ in range(n)]
    c.sort()
    for l,r,real in c:
        if l <=k<=r and k < real:
            k=real
    print(k)