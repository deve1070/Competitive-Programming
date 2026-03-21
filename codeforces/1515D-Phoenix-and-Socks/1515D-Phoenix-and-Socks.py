from collections import Counter

for i in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = n // 2
    swp = abs(r - l) // 2
    c = Counter(a[:l])
    d = Counter(a[l:])
    if l < r:
        l, r = r, l
        c, d = d, c
    x = 0
    for i in c:
        m = min(c[i], d[i])
        c[i] -= m
        d[i] -= m
        cnt -= m
    for i in c:
        x += c[i] // 2
    print(cnt + max(0, (swp - x)))