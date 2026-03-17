import sys
input=sys.stdin.readline
def solve():
    s = input().strip()
    t = input().strip()
    mapp = [0]*26
    for c in t:
        mapp[ord(c)-97]+=1
    for c in s:
        mapp[ord(c)-97]-=1
    for i in range(26):
        if mapp[i]<0:
            print('Impossible')
            return
    i = 0
    ans = ''
    for j in range(26):
        while i<len(s) and ord(s[i])-97<=j:
            ans+=s[i]
            i+=1
        ans+=chr(j+97)*mapp[j]
    print(ans)
for _ in range(int(input())):
    solve()