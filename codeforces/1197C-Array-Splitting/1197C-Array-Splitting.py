n,k=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(n-1):
    l.append(a[i+1]-a[i])
l.sort()
print(sum(l[:n-k]))