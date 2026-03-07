def f(s, x):
    for t, c in enumerate(s, 1):
        x += -1 if c == "L" else 1
        if x == 0:
            return t
    return float('inf')

for _ in range(int(input())):
    n, x, k = map(int, input().split())
    o = input()
    
    f1 = f(o, x)
    print(0 if f1 > k else 1 + int((k - f1) // f(o, 0)))