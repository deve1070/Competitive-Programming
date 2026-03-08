input()
r=0
for x in sorted(map(int,input().split())):r+=x>r
print(r)