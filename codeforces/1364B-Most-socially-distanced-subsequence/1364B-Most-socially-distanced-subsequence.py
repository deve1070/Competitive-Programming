import sys
input=sys.stdin.readline
for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	a=[]
	for i in range(n):
		if i==0 or i==n-1:
			a.append(l[i])
		elif ((l[i]>l[i-1])^(l[i+1]>l[i])):
		    a.append(l[i])
	print(len(a))
	print(*a)