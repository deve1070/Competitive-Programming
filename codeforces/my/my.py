t=int(input())
for _ in range(t):
    num=int(input())
    _sum=0
    while num > 0:
        _sum += num%10
        num //=10
    print(_sum)