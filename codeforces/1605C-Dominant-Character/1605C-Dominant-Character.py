#for s in[*open(0)][2::2]:
    n=int(input())
    s=input()
    a=-1
    for i in"abbacca","accabba","acba","abca","aca","aba","aa":
	    if i in s:a=len(i)
    print(a)